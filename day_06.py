#%% Initialize
import numpy as np
from collections import Counter

#%% Read input
with open("day_06_input.txt") as f:
    fish_state = [int(x) for x in f.read().split(",")]

#%% Part 1
fish_array = np.array(fish_state)
for i in range(80):
    fish_array -= 1
    fish_array = np.hstack([fish_array, np.ones(np.count_nonzero(fish_array < 0)) * 8])
    fish_array[fish_array < 0] = 6
print(len(fish_array))

#%% Part 2
fish_dict = Counter(fish_state)
for i in range(256):
    new_fish_dict = Counter()
    for j in range(8):
        new_fish_dict[j] = fish_dict[j+1]
    new_fish_dict[8] = fish_dict[0]
    new_fish_dict[6] += fish_dict[0]
    fish_dict = new_fish_dict

print(sum(fish_dict.values()))
