import time
import re

begin = time.time()

###


def valid_year(least: int, most: int):
    def validator(i: str):
        d = int(i) if i.isdigit() else False
        if not d or len(i) != 4:
            return False
        return least <= d <= most

    return validator


def valid_measure(i: str):
    match = re.match(r"(?P<num>\d*)(?P<unit>cm|in)", i)
    if not match:
        return False
    g = match.groupdict()
    unit = g["unit"]
    num_s = g["num"]
    num = int(num_s) if num_s.isdigit() else 0
    if unit == "cm":
        return 150 <= num <= 193
    elif unit == "in":
        return 59 <= num <= 76


def valid_color(i: str):
    return bool(re.match(r"#[0-9a-f]{6}", i))


def valid_eye_color(i: str):
    return i in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def valid_pass_id(i: str):
    return bool(re.match(r"^\d{9}$", i))


validators = {
    "byr": valid_year(least=1920, most=2002),
    "iyr": valid_year(least=2010, most=2020),
    "eyr": valid_year(least=2020, most=2030),
    "hgt": valid_measure,
    "hcl": valid_color,
    "ecl": valid_eye_color,
    "pid": valid_pass_id,
    "cid": lambda _: True,
}

with open("input.txt") as file:
    passStrings = list(map(lambda l: l.replace("\n", " "), file.read().split("\n\n")))


def parse_passport(s: str):
    p = re.compile(r"(?P<key>\w{3}):(?P<val>[^ ]*) ?")
    i = re.finditer(p, s)
    d = {}
    for m in i:
        g = m.groupdict()
        d[g["key"]] = g["val"]
    return d


def validate(pp, quick: bool = False):
    keys = pp.keys()
    if len(keys) != 8 and not (len(keys) == 7 and "cid" not in pp):
        return False
    if quick:
        return True

    for key in keys:
        if not (validators[key](pp[key])):
            return False
    return True


passports = [
    parse_passport(s) for s in passStrings if validate(parse_passport(s), True)
]
valid_passports = [
    parse_passport(s) for s in passStrings if validate(parse_passport(s))
]
print(f"Valid passports, quick check: {len(passports)}")
print(f"Valid passports, value check: {len(valid_passports)}")

###

end = time.time()
print(f"Runtime: {(end - begin) / 1000}ms")
