#%% Initialize
import numpy as np

#%% Read input
with open("day_11_input.txt") as f:
    octopus_grid = np.genfromtxt(f, dtype=int, delimiter=1)


#%% Common
def simulate_step(grid):
    grid += 1
    total_flashed = 0
    flashed = set()
    flashing = set(zip(*np.where(grid > 9)))
    while flashing:
        for x, y in flashing:
            grid[max(x - 1, 0):min(x + 2, 10), max(y - 1, 0):min(y + 2, 10)] += 1
        flashed.update(flashing)
        total_flashed += len(flashing)
        flashing = set(zip(*np.where(grid > 9))) - flashed

    grid[grid > 9] = 0
    return total_flashed


#%% Part 1
current_grid = octopus_grid.copy()
print(sum(simulate_step(current_grid) for _ in range(100)))

#%% Part 2
current_grid = octopus_grid.copy()
i = 0
while not (current_grid == 0).all():
    simulate_step(current_grid)
    i += 1
print(i)
