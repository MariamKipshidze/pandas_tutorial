import pandas as pd

a = [3, 7, 12]
my_var_1 = pd.Series(a)

print(my_var_1)
print(my_var_1[0])
print(my_var_1[1])

b = [1, 7, 2]
my_var_2 = pd.Series(b, index = ["x", "y", "z"])

print(my_var_2)
print(my_var_2["y"])
print(my_var_2["z"])

calories = {"day1": 420, "day2": 380, "day3": 390}
my_var_3 = pd.Series(calories, name = "calories")

print(my_var_3)
print(my_var_3["day3"])
print(my_var_3["day2"])
print(my_var_3.dtypes)
print(my_var_3.shape)
print(my_var_3.index)
print(len(my_var_3))

calories = {"day1": 420, "day2": 380, "day3": 390}
my_var_4 = pd.Series(calories, index = ["day1", "day2"], dtype = float)

print(my_var_4)
print(my_var_4["day1"])
print(my_var_4["day2"])


# describe()
print(my_var_3.describe())

# Example Series
s = pd.Series([10, 20, 30, 40, 50, None])

# Get descriptive statistics
count = s.count()
mean = s.mean()
std = s.std()
min_val = s.min()
q25 = s.quantile(0.25)
median = s.median()
q75 = s.quantile(0.75)
max_val = s.max()

# Print them
print(f"Count: {count}")
print(f"Mean: {mean}")
print(f"Std: {std}")
print(f"Min: {min_val}")
print(f"25%: {q25}")
print(f"50% (Median): {median}")
print(f"75%: {q75}")
print(f"Max: {max_val}")

