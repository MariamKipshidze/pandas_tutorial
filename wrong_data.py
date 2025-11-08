import pandas as pd

df = pd.read_csv('data_2.csv')
df.loc[7,'Duration'] = 45

print(df.to_string())


df = pd.read_csv('data_2.csv')

for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120

print(df.to_string())


df = pd.read_csv('data_2.csv')

for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.drop(x, inplace = True)

print(df.to_string())

df = pd.read_csv('data_2.csv')
print(df.duplicated())
df.drop_duplicates(inplace = True)
