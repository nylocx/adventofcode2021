#%% Initialize
import math
import re

#%% Read input
with open("day_17_input.txt") as f:
    x1, x2, y1, y2 = map(int, re.findall(r"(-?\d+)", f.read()))

#%% Part 1
x = 0
y = 0
x_velocity = math.ceil((math.sqrt(8 * x1 + 1) - 1) / 2)
y_velocity = abs(y1) - 1
max_y = 0
while True:
    x += x_velocity
    y += y_velocity
    if y > max_y:
        max_y = y
    x_velocity += 1 if x_velocity < 0 else -1 if x_velocity > 0 else 0
    y_velocity -= 1
    if (x1 <= x <= x2) and (y1 <= y <= y2):
        break

print(max_y)

#%% Part 2
possible_solutions = 0
for i in range(math.ceil((math.sqrt(8 * x1 + 1) - 1) / 2), x2 + 1):
    for j in range(y1, abs(y1)):
        x = 0
        y = 0
        x_velocity = i
        y_velocity = j
        while True:
            x += x_velocity
            y += y_velocity
            x_velocity += 1 if x_velocity < 0 else -1 if x_velocity > 0 else 0
            y_velocity -= 1
            if (x1 <= x <= x2) and (y1 <= y <= y2):
                possible_solutions += 1
                break
            elif x > x2 or y < y1:
                break

print(possible_solutions)
