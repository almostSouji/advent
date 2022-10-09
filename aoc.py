#!/usr/bin/env python3
import sys
from dotenv import load_dotenv
from os import getenv
import requests
from datetime import date
from bs4 import BeautifulSoup
import argparse

load_dotenv()


def url(year, day, solution, progress, input):
    if input:
        return f"https://adventofcode.com/{year}/day/{day}/input"
    if progress:
        return f"https://adventofcode.com/{year}/leaderboard/self"
    if solution != None:
        return f"https://adventofcode.com/{year}/day/{day}/answer"
    else:
        return f"https://adventofcode.com/{year}/day/{day}"


parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument(
    "-s", "--solution", help="Submit solution", metavar="<solution>", nargs=1
)
parser.add_argument(
    "-y",
    "--year",
    type=int,
    default=date.today().year,
    help="Target year since 2015",
    metavar="year",
    choices=range(2015, 2023),
)
parser.add_argument("-p2", "--part2", help="Solve part 2", action="store_true")
parser.add_argument("-p", "--progress", help="Show progress table", action="store_true")
parser.add_argument("-i", "--input", help="Pull puzzle input", action="store_true")
parser.add_argument(
    "-d",
    "--day",
    type=int,
    default=date.today().day,
    help="Day (1, 25)",
    metavar="day",
    choices=range(1, 26),
)
args = parser.parse_args()
config = vars(args)

session_key = getenv("USER_SESSION")
if (session_key == None):
    print("Missing environment variable value for USER_SESSION!")
    exit(1)

year, day, p2, solution, prog, inp = (
    config["year"],
    config["day"],
    config["part2"],
    config["solution"],
    config["progress"],
    config["input"],
)

use_answer = solution != None

res = (
    requests.post(
        url(year, day, solution, prog, inp),
        cookies={"session": session_key},
        data={"level": 2 if p2 else 1, "answer": solution},
    )
    if use_answer
    else requests.get(
        url(year, day, solution, prog, inp),
        cookies={"session": session_key},
    )
)

if res.status_code != 200:
    print(
        f"Failed to fetch {day}/12/{year}. Are you sure that that's correct?",
        file=sys.stderr,
    )
    exit(1)

soup = BeautifulSoup(res.text, features="html.parser")

if inp:
    print(res.text)
    print(soup.get_text().rstrip(), end="")
elif prog:
    if (soup.pre == None):
        print("Cannot Parse response as expected, the structure might have changed!")
        exit(1)
    print(soup.pre.get_text().strip())
elif use_answer:
    if (soup.main == None):
       print("Cannot Parse response as expected, the structure might have changed!")
       exit(1)
    print(soup.main.get_text().strip())
else:
    ans = []
    for article in soup.select("article"):
        h = article.select_one("h2").get_text()
        ps = [p.get_text() for p in article.select("p, pre, ul, ol")]
        ans.append(h + "\n" + "\n\n".join(ps))

    print("\n\n".join(ans))
