#%% Initialize
import math
import numpy as np
from skimage.morphology import flood_fill

#%% Read input
with open("day_09_input.txt") as f:
    height_map = np.genfromtxt(f, delimiter=1, dtype=int)

#%% Part 1
padded_height_map = np.pad(height_map, pad_width=1, mode="constant", constant_values=9)
local_minima = (
    (padded_height_map < np.roll(padded_height_map, 1, 0))
    & (padded_height_map < np.roll(padded_height_map, -1, 0))
    & (padded_height_map < np.roll(padded_height_map, 1, 1))
    & (padded_height_map < np.roll(padded_height_map, -1, 1))
)
np.sum(padded_height_map[local_minima] + 1)

#%% Part 2
xs, ys = np.where(local_minima[1:-1, 1:-1])
basins = []
flood_map = np.zeros_like(height_map)
for x, y, height in zip(xs, ys, height_map[xs, ys]):
    flood_map[(height_map >= height) & (height_map < 9)] = -1
    basins.append(
        np.count_nonzero(flood_fill(flood_map, (x, y), 10, connectivity=1) == 10)
    )

math.prod(sorted(basins, reverse=True)[:3])
