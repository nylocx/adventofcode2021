#%% Initialize
import numpy as np

#%% Read input
with open("day_13_input.txt") as f:
    dots = []
    while (l := f.readline()) != "\n":
        dots.append(map(int, l.split(",")))

    folds = [
        (axis, int(index))
        for axis, index in (line.split()[-1].split("=") for line in f)
    ]

#%% Common
xs, ys = zip(*dots)

size = (
    max([y for a, y in folds if a == "y"]) * 2 + 1,
    max([x for a, x in folds if a == "x"]) * 2 + 1,
)

#%% Part 1
paper = np.zeros(size)
paper[ys, xs] = 1
axis, fold = folds[0]
if axis == "y":
    paper = paper[:fold, :] + np.flipud(paper[fold + 1:, :])
else:
    paper = paper[:, :fold] + np.fliplr(paper[:, fold + 1:])

np.count_nonzero(paper)

#%% Part 2
paper = np.zeros(size)
paper[ys, xs] = 1
for axis, fold in folds:
    paper = (
        paper[:fold, :] + np.flipud(paper[fold + 1:, :])
        if axis == "y"
        else paper[:, :fold] + np.fliplr(paper[:, fold + 1:])
    )

for row in (paper > 0).astype(int):
    print(*["#" if x > 0 else " " for x in row])
