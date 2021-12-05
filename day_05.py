#%% Initialize
import numpy as np

#%% Read input
with open("day_05_input.txt") as f:
    lines = np.array(
        [[[int(y) for y in x.split(",")] for x in line.split("->")] for line in f]
    )


#%% Common
def count_overlaps(input_lines):
    grid = np.zeros((input_lines[:, :, 0].max() + 1, input_lines[:, :, 1].max() + 1))
    for line in input_lines:
        (x1, y1), (x2, y2) = line
        if x1 == x2:
            grid[x1, min(y1, y2) : max(y1, y2) + 1] += 1
        elif y1 == y2:
            grid[min(x1, x2) : max(x1, x2) + 1, y1] += 1
        else:
            grid[
                np.linspace(x1, x2, abs(x1 - x2) + 1, endpoint=True, dtype=int),
                np.linspace(y1, y2, abs(x1 - x2) + 1, endpoint=True, dtype=int),
            ] += 1

    return np.count_nonzero(grid > 1)


#%% Part 1
straight_lines = lines[
    np.where((lines[:, 0, 0] == lines[:, 1, 0]) | (lines[:, 0, 1] == lines[:, 1, 1]))
]

count_overlaps(straight_lines)

#%% Part 2
count_overlaps(lines)
