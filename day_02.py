#%% Initialize
import pandas as pd

#%% Read input
with open("day_02_input.txt") as f:
    _input = list(map(lambda x: (x[0], int(x[1])), (x.split() for x in f)))

#%% Part 1
horizontal = 0
depth = 0
for direction, amount in _input:
    if direction == "forward":
        horizontal += amount
    elif direction == "down":
        depth += amount
    else:
        depth -= amount

print("Result of depth times horizontal (Part 1):", depth * horizontal)


#%% Part 2
horizontal = 0
depth = 0
aim = 0
for direction, amount in _input:
    if direction == "forward":
        horizontal += amount
        depth += aim * amount
    elif direction == "down":
        aim += amount
    else:
        aim -= amount

print("Result of depth times horizontal (Part 2):", depth * horizontal)

#%% Part 1 (pandas)
df = pd.read_csv("day_02_input.txt", sep=" ", header=None)
d, f, u = df.groupby(0).sum().to_numpy()
print((d-u)*f)
