#!/usr/bin/env python3
import sys
import pprint
import copy
from math import lcm


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


def p_monkeys(monkeys):
    for i, monkey in enumerate(monkeys):
        debug("monkey", i, monkey["items"],
              "inspections:", monkey["inspections"])

####


monkeys = []

for (i, raw_line) in enumerate(sys.stdin):
    line = raw_line.strip()

    m_index = i // 7
    if (len(monkeys) - 1 < m_index):
        monkeys.append({})

    match (i % 7):
        case 0:
            monkeys[m_index]["inspections"] = 0
        case 1:
            monkeys[m_index]["items"] = list(reversed([int(x) for x in line.split(":")[
                1].strip().split(",")]))
        case 2:
            # operation
            monkeys[m_index]["operation"] = tuple(
                line.split("=")[1].strip().split(" ")[1:])
        case 3:
            # test
            monkeys[m_index]["div"] = int(line.split("by")[1])
        case 4:
            # if true
            monkeys[m_index]["if_true"] = int(line.split("monkey")[1])
        case 5:
            # if false
            monkeys[m_index]["if_false"] = int(line.split("monkey")[1])


def iterate(monkeys, rounds, worry_decrease):
    for round in range(rounds):
        for monkey in monkeys:
            for _ in range(len(monkey["items"])):
                item = monkey["items"].pop()
                monkey["inspections"] += 1

                match (monkey["operation"]):
                    case "*", "old":
                        item *= item
                    case "+", "old":
                        item += item
                    case "*", x:
                        item *= int(x)
                    case "+", x:
                        item += int(x)

                item = worry_decrease(item)

                next_monkey = monkey["if_true"] if item % monkey["div"] == 0 else monkey["if_false"]
                next_items = monkeys[next_monkey]["items"]
                monkeys[next_monkey]["items"] = [item] + next_items

    top, snd = sorted([monkey["inspections"] for monkey in monkeys])[-2:]
    print(top * snd)


iterate(copy.deepcopy(monkeys), 20, lambda x: x // 3)

monkey_lcm = lcm(*[monkey["div"] for monkey in monkeys])
iterate(copy.deepcopy(monkeys), 10_000, lambda x: x % monkey_lcm)
