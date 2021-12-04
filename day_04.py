#%% Initialize
import numpy as np
import pandas as pd

#%% Read input
with open("day_04_input.txt") as f:
    numbers = [int(x) for x in f.readline().split(",")]
    boards = pd.read_csv(f, sep=r"\s+", engine="python", header=None)
boards = np.array_split(boards, len(boards) // 5)


#%% Common
def winner_boards(current_pick: list[int]):
    result = []
    for board in boards:
        hits = board.isin(current_pick)
        result.append(hits.all(axis=1).any() or hits.all(axis=0).any())
    return result


#%% Part 1
for i in range(1, len(numbers)):
    current_numbers = numbers[:i]
    winner = winner_boards(current_numbers)
    if any(winner):
        winner_board = boards[winner.index(True)]
        print(
            int(winner_board[~winner_board.isin(current_numbers)].sum().sum())
            * current_numbers[-1]
        )
        break

#%% Part 2
last_winner = []
for i in range(1, len(numbers)):
    current_numbers = numbers[:i]
    winner = winner_boards(current_numbers)
    if all(winner):
        winner_board = boards[last_winner.index(False)]
        print(
            int(winner_board[~winner_board.isin(current_numbers)].sum().sum())
            * current_numbers[-1]
        )
        break
    last_winner = winner
