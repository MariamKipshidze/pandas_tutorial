import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df_1 = pd.DataFrame(data)
print(df_1)
print(df_1.loc[0])
print(df_1.loc[[0, 1]])

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df_2 = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df_2)
print(df_2.loc["day1"])
print(df_2.loc[["day1", "day2"]])
