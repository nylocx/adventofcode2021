#%% Initialize
import re

#%% Read input
with open("day_08_input.txt") as f:
    patterns, outputs = zip(*[x.strip().split(" | ") for x in f.readlines()])

#%% Part 1
print(sum(len(x) in [2, 3, 4, 7] for x in (re.findall("[abcdefg]+", " ".join(outputs)))))

#%% Part 2
output_sum = 0
for pattern, output in zip(patterns, outputs):
    digits = [frozenset(x) for x in sorted(pattern.split(), key=len)]
    # known patterns
    mapping = {1: digits[0], 7: digits[1], 4: digits[2], 8: digits[9]}
    # length 5 pattern
    for i in range(3, 6):
        digit = digits[i]
        if mapping[1].issubset(digit):
            mapping[3] = digit
        elif len(mapping[4] & digit) == 2:
            mapping[2] = digit
        else:
            mapping[5] = digit
    # length 6 pattern
    for i in range(6, 9):
        digit = digits[i]
        if mapping[3].issubset(digit):
            mapping[9] = digit
        elif mapping[1].issubset(digit):
            mapping[0] = digit
        else:
            mapping[6] = digit

    reverse_mapping = {v: str(k) for k, v in mapping.items()}
    output_sum += int("".join(reverse_mapping[frozenset(x)] for x in output.split()))
print(output_sum)
