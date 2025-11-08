import pandas as pd

df = pd.read_csv('data.csv')
new_df = df.dropna()
print(new_df.to_string())

df = pd.read_csv('data.csv')
df.dropna(inplace = True) # If you want to change the original DataFrame, use the inplace = True argument
print(df.to_string())

# Replace Empty Values
df = pd.read_csv('data.csv')
df.fillna(130, inplace = True)

# Replace Only For Specified Columns
df = pd.read_csv('data.csv')
df.fillna({"Calories": 130}, inplace=True)

# Replace Using Mean, Median, or Mode
df = pd.read_csv('data.csv')
x = df["Calories"].mean()
df.fillna({"Calories": x}, inplace=True)

x = df["Calories"].mode()[0]
x = df["Calories"].median()
