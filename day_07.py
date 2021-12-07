#%% Initialize
import numpy as np

#%% Read input
with open("day_07_input.txt") as f:
    positions = np.array([int(x) for x in f.readline().split(",")])

#%% Part 1
print(int(np.abs(positions - np.median(positions).round()).sum()))

#%% Part 2
mean_diff = np.abs(positions - np.floor(np.mean(positions)))
print(int((mean_diff * (mean_diff + 1) / 2).sum()))
