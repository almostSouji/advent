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
alphabet2 = list("AKQT98765432J")
alphabet.reverse()
alphabet2.reverse()


def score_hand(cards, joker=False):
    counter = {}
    for card in cards:
        counter[card] = counter.get(card, 0) + 1
    jokers = counter.get("J", 0)

    vals = (
        [x[1] for x in counter.items() if x[0] != "J"]
        if joker
        else list(counter.values())
    )
    vals.sort(reverse=True)

    if joker and len(vals):
        vals[0] += jokers

    if joker and jokers == 5:  # Five of a kind (all jokers)
        return 7

    elif vals[0] == 5:  # Five of a kind
        return 7

    elif vals[0] == 4:  # Four of a kind
        return 6

    elif vals[0] == 3 and vals[1] == 2:  # Full house
        return 5

    elif vals[0] == 3:  # Three of a kind
        return 4

    elif vals[0] == 2 and vals[1] == 2:  # Two pair
        return 3

    elif vals[0] == 2:  # One pair
        return 2

    else:  # High card
        return 1


def card_strength(card, joker=False):
    return alphabet2.index(card) if joker else alphabet.index(card)


def sort(a, b, joker=False):
    a_cards, a_score, _ = a
    b_cards, b_score, _ = b

    if a_score > b_score:
        return 1
    elif a_score < b_score:
        return -1
    else:
        for i, c in enumerate(a_cards):
            a_s = card_strength(c, joker)
            b_s = card_strength(b_cards[i], joker)

            if a_s > b_s:
                return 1
            if a_s < b_s:
                return -1
        return 0


def evaluate_hands(hands):
    res = 0
    for i, (_, _, bid) in enumerate(hands):
        rank = len(hands) - i
        res += rank * bid
    return res


hands = []
hands2 = []
for line in open(0):
    cards, bid = line.strip().split()
    bid = int(bid)

    hands.append((cards, score_hand(cards), bid))
    hands2.append((cards, score_hand(cards, joker=True), bid))


hands.sort(key=cmp_to_key(sort), reverse=True)
hands2.sort(key=cmp_to_key(lambda a, b: sort(a, b, joker=True)), reverse=True)


s = evaluate_hands(hands)
print(s)

s2 = evaluate_hands(hands2)
print(s2)

assert s == 250254244, s
assert s2 == 250087440, s2
