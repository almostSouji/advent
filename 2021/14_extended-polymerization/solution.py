import time
begin = time.time()

###

with open("./input.txt", "r") as file:
    ns = list(map(lambda x: x.strip(), file.readlines()))
    template = ns[0]
    rules = {}

    for l in ns[2:]:
        (a, b) = l.split(" -> ")
        rules[a] = b


def score(d, template):
    c = {
        template[0]: 1,
        template[-1]: 1
    }
    for k, v in d.items():
        a, b = k
        inc(c, a, v)
        inc(c, b, v)
    for k, v in c.items():
        c[k] = int(c[k]/2)

    vals = list(c.values())
    return max(vals) - min(vals)


def inc(d, k, n):
    if k in d:
        d[k] += n
    else:
        d[k] = n


def split(template):
    prev = template[0]
    res = {}
    for e in template[1:]:
        inc(res, prev+e, 1)
        prev = e
    return res


def step(c, rules):
    for k, v in list(c.items()):
        a, b = k
        inc(c, k, -v)
        inc(c, a+rules[k], v)
        inc(c, rules[k]+b, v)


def solve1(template, rules):
    c = split(template)
    for i in range(10):
        step(c, rules)
    return score(c, template)


def solve2(template, rules):
    c = split(template)
    for i in range(40):
        step(c, rules)
    return score(c, template)


print(f"Part 1: {solve1(template, rules)}")
print(f"Part 2: {solve2(template, rules)}")

###

end = time.time()
print(f"Runtime: {(end - begin) * 1000}ms")
