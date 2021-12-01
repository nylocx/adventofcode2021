#  --- Day 1: Sonar Sweep ---
#%% Initialization
import pandas as pd

#%% Read input
depths = pd.read_csv("day_01_input.txt", header=None).squeeze()

#%% Part 1
number_of_increases = sum(depths.diff() > 0)
print("Number of depth increases:", number_of_increases)

#%% Part 2
number_of_sum_increases = sum(depths.rolling(3).sum().diff() > 0)
print("Number of depth sum increases:", number_of_sum_increases)
