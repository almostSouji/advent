#!/usr/bin/env python3

alphabet = list("AKQJT98765432")
alphabet2 = list("AKQT98765432J")
alphabet.reverse()
alphabet2.reverse()


def score_hand(cards, joker=False):
    vals = [cards.count(x) for x in set(cards) if (x != "J" if joker else True)]
    vals.sort(reverse=True)
    jokers = cards.count("J")

    if joker and len(vals):
        vals[0] += jokers

    if joker and jokers == 5:
        return [5]

    return vals


def card_strength(card, joker=False):
    return alphabet2.index(card) if joker else alphabet.index(card)


def sort(val, joker=False):
    return (val[1], [card_strength(x, joker) for x in val[0]])


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


hands.sort(key=sort, reverse=True)
hands2.sort(key=lambda x: sort(x, joker=True), reverse=True)

s = evaluate_hands(hands)
print(s)

s2 = evaluate_hands(hands2)
print(s2)

assert s == 250254244, s
assert s2 == 250087440, s2
