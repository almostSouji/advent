#!/usr/bin/env python3
import sys
import pprint
import re
from collections import deque


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


def solve(coo, coc, coob, cog, ccob, cobg, time):
    # ore, clay, obsidian, geodes, orebots, claybots, obsidianbots, geodebots, time
    initial_state = (0, 0, 0, 0, 1, 0, 0, 0, time)
    q = deque([initial_state])
    seen = set()
    best = 0

    while q:
        state = o, c, ob, g, b1, b2, b3, b4, t = q.popleft()
        best = max(best, g)

        if t == 0:
            continue

        # do not consider more robots than what can be spent in a round and material
        # since robots generate 1 material per round

        max_ore = max(coo, coc, coob, cog)

        b1 = min(max_ore, b1)
        b2 = min(ccob, b2)
        b3 = min(cobg, b3)
        # always need more geodes!

        # discard material that cannot be spent
        # max ore that can be spent in time
        # subtract ore that will be generated by bots
        o = min(o, max_ore*time - b1*(t-1))
        c = min(c, ccob*time - b2*(t-1))
        ob = min(ob, cobg*time - b3*(t-1))
        # always need more geodes!

        state = (o, c, ob, g, b1, b2, b3, b4, t)
        if state in seen:
            continue
        seen.add(state)

        # debug

        # do nothing := spend 1 time, existing bots generate minerals
        q.append((o+b1, c+b2, ob+b3, g+b4, b1, b2, b3, b4, t-1))

        assert all(x >= 0 for x in [o, c, ob, g]), state
        # check minerals do decide of we can build a bot
        if o >= coo:
            # build ore bot := gain bot, spend resources, spend 1 time, existing bots generate minerals
            q.append((o+b1-coo, c+b2, ob+b3, g+b4, b1+1, b2, b3, b4, t-1))
        if o >= coc:
            # build clay bot := gain bot, spend resources, spend 1 time, existing bots generate minerals
            q.append((o+b1-coc, c+b2, ob+b3, g+b4, b1, b2+1, b3, b4, t-1))
        if o >= coob and c >= ccob:
            # build obsidian bot := gain bot, spend resources, spend 1 time, existing bots generate minerals
            q.append((o+b1-coob, c+b2-ccob, ob+b3, g+b4, b1, b2, b3+1, b4, t-1))
        if o >= cog and ob >= cobg:
            # build geode bot := gain bot, spend resources, spend 1 time, existing bots generate minerals
            q.append((o+b1-cog, c+b2, ob+b3-cobg, g+b4, b1, b2, b3, b4+1, t-1))

    return best


t = 0
for i, line in enumerate(open(0)):
    i, oo, co, obo, obc, go, gob = map(int, re.findall(r"\d+", line))

    debug((i, oo, co, obo, obc, go, gob))
    # [ore, clay, obsidian, geode]
    res = solve(oo, co, obo, go, obc, gob, 24)
    debug(res)
    t += res * i

print(f"p1: {t}")
