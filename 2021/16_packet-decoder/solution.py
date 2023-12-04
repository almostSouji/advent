import time

begin = time.time()

###

with open("./test2.txt", "r") as file:
    ns = file.readline()

hex_to_bin = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}

bin_to_hex = {
    "0000": "0",
    "1": "1",
    "10": "2",
    "11": "3",
    "100": "4",
    "101": "5",
    "110": "6",
    "111": "7",
    "1000": "8",
    "1001": "9",
    "1010": "A",
    "1011": "B",
    "1100": "C",
    "1101": "D",
    "1110": "E",
    "1111": "F",
}


def parse_packet_info(p):
    ver = int(p[0:3], 2)
    p_type = int(p[3:6], 2)
    return (ver, p_type)


# packet: (version, type, packets, value)
# parse: (bits, pointer, packet)


def parse(bits, pointer, parent):
    (v, t) = parse_packet_info(bits[pointer:])
    print(f"version: {v} type: {t}")
    pointer += 6

    match t:
        case 4:
            # literal
            res = ""
            for i in range(pointer, len(bits), 5):
                chunk = bits[i : i + 5]
                last = False if chunk[0] == "1" else True
                res += chunk[1:]
                if last:
                    new_node = (v, t, [], int(res, 2))
                    if len(parent) > 0:
                        parent[2].append(new_node)
                        return parent
                    else:
                        return new_node
        case _:
            mode = bits[pointer]
            pointer += 1
            match mode:
                case "0":
                    # 15 bits -> length in bits
                    l_subp = int(bits[pointer : pointer + 16], 2)
                    pointer += 15
                case "1":
                    # 11 bits -> number of subpackets immediately contained
                    n_subp = int(bits[pointer : pointer + 12], 2)
                    pointer += 11
                    n = 0
                    new_node = (v, t, [], 0)
                    while n < n_subp:
                        new_node[2].append(parse(bits, pointer, new_node))
                    if (len(parent)) > 0:
                        print(parent)
                        parent[2].append(new_node)
                        return parent
                    else:
                        return new_node


def solve1(ns):
    binary = ""
    for n in ns:
        binary += hex_to_bin[n]
    print(binary)
    print(parse(binary, 0, ()))


def solve2(ns):
    0


print(f"Part 1: {solve1(ns)}")
print(f"Part 2: {solve2(ns)}")

###

end = time.time()
print(f"Runtime: {(end - begin) * 1000}ms")
