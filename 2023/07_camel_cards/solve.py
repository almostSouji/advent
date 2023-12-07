#!/usr/bin/env python3
import sys
import pprint
from functools import cmp_to_key


def debug(*args, pretty=False, **kwargs):
    "print() to stderr for debuggin purposes"
    if pretty:
        pprint.pprint(*args, **kwargs, stream=sys.stderr)
    else:
        print(
            *args,
            **kwargs,
            file=sys.stderr,
        )


####

alphabet = list("AKQJT98765432")
alphabet.reverse()

hands = []
for line in open(0):
    cards, bid = line.strip().split()
    bid = int(bid)

    score = 0
    counter = {}
    for card in cards:
        current = counter.get(card, 0)
        counter[card] = current + 1

    vals = list(counter.values())
    vals.sort(reverse=True)

    if vals[0] == 5:  # Five of a kind
        score = 7
    elif vals[0] == 4:  # Four of a kind
        score = 6

    elif vals[0] == 3 and vals[1] == 2:  # Full house
        score = 5

    elif vals[0] == 3:  # Three of a kind
        score = 4

    elif vals[0] == 2 and vals[1] == 2:  # Two pair
        score = 3

    elif vals[0] == 2:  # One pair
        score = 2
    else:  # High card
        score = 1

    hands.append((cards, score, bid))


def card_strength(card):
    return alphabet.index(card)


def sort(a, b):
    a_cards, a_score, _ = a
    b_cards, b_score, _ = b

    if a_score > b_score:
        return 1
    elif a_score < b_score:
        return -1
    else:
        for i, c in enumerate(a_cards):
            a_s = card_strength(c)
            b_s = card_strength(b_cards[i])

            if a_s > b_s:
                return 1
            if a_s < b_s:
                return -1
        return 0


hands.sort(key=cmp_to_key(sort), reverse=True)

s = 0

for i, (cards, score, bid) in enumerate(hands):
    rank = len(hands) - i
    s += rank * bid

print(s)

assert s == 250254244, s
