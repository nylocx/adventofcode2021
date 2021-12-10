#%% Initialize
from collections import deque

#%% Read input
with open("day_10_input.txt") as f:
    lines = [x.strip() for x in f]

#%% Common
open_literals_map = dict(zip("([{<", ")]}>"))
close_literals_map = dict(zip(")]}>", "([{<"))

#%% Part 1
points = 0
point_map = {")": 3, "]": 57, "}": 1197, ">": 25137}
for line in lines:
    brace_stack = deque()
    for c in line:
        if c in open_literals_map:
            brace_stack.append(c)
        elif c in close_literals_map:
            if not brace_stack or brace_stack.pop() != close_literals_map[c]:
                points += point_map[c]
                break

print(points)

#%% Part 2
points = []
point_map = {")": 1, "]": 2, "}": 3, ">": 4}
for line in lines:
    brace_stack = deque()
    line_points = 0
    for c in line:
        if c in open_literals_map:
            brace_stack.append(c)
        elif c in close_literals_map:
            if not brace_stack or brace_stack.pop() != close_literals_map[c]:
                brace_stack.clear()
                break

    while brace_stack:
        line_points = line_points * 5 + point_map[open_literals_map[brace_stack.pop()]]
    if line_points:
        points.append(line_points)

print(sorted(points)[len(points) // 2])
