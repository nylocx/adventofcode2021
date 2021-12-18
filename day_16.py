#%% Initialize
import math

#%% Read input
with open("day_16_input.txt") as f:
    bits = "".join(f"{int(x, 16):0>4b}" for x in f.readline().strip())


#%% Part 1
def parse_part1(start):
    i = start
    version_sum = int(bits[i : i + 3], 2)
    packet_type = int(bits[i + 3 : i + 6], 2)
    i += 6
    if packet_type == 4:
        while True:
            i += 5
            if bits[i - 5] == "0":
                break
    else:
        if bits[i] == "0":
            last_i = i + 16 + int(bits[i + 1 : i + 16], 2)
            i += 16
            while i < last_i:
                i, v = parse_part1(i)
                version_sum += v
        else:
            num_sub_packets = int(bits[i + 1 : i + 12], 2)
            i += 12
            for _ in range(num_sub_packets):
                i, v = parse_part1(i)
                version_sum += v

    return i, version_sum


parse_part1(0)

#%% Part 2
operator = [
    sum,
    math.prod,
    min,
    max,
    lambda x: x[0],
    lambda x: x[0] > x[1],
    lambda x: x[0] < x[1],
    lambda x: x[0] == x[1],
]


def parse_part2(start):
    i = start
    packet_type = int(bits[i + 3 : i + 6], 2)
    i += 6
    if packet_type == 4:
        value_bits = ""
        while True:
            value_bits += bits[i + 1 : i + 5]
            i += 5
            if bits[i - 5] == "0":
                break
        values = [int(value_bits, 2)]
    else:
        values = []
        if bits[i] == "0":
            last_i = i + 16 + int(bits[i + 1 : i + 16], 2)
            i += 16
            while i < last_i:
                i, v = parse_part2(i)
                values.append(v)
        else:
            num_sub_packets = int(bits[i + 1: i + 12], 2)
            i += 12
            for _ in range(num_sub_packets):
                i, v = parse_part2(i)
                values.append(v)

    return i, operator[packet_type](values)


parse_part2(0)
