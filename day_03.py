#%% Initialize
import pandas as pd

#%% Read input
df = pd.read_fwf("day_03_input.txt", widths=[1]*12, header=None)

#%% Part 1
gamma = "".join(df.mode().astype(str).iloc[0])
epsilon = "".join("01"[x == "0"] for x in gamma)

print("Power consumption:", int(gamma, 2) * int(epsilon, 2))

#%% Part 2
df_oxygen = df.copy()
df_co2 = df.copy()
for i in range(12):
    if len(df_oxygen) > 1:
        df_oxygen = df_oxygen[df_oxygen[i] == df_oxygen[i].mode().max()]
    if len(df_co2) > 1:
        df_co2 = df_co2[df_co2[i] != df_co2[i].mode().max()]
oxygen = "".join(df_oxygen.iloc[0].astype(str))
co2 = "".join(df_co2.iloc[0].astype(str))

print("Life support rating:", int(oxygen, 2) * int(co2, 2))

