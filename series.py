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

calories = {"day1": 420, "day2": 380, "day3": 390}
my_var_4 = pd.Series(calories, index = ["day1", "day2"], dtype = float)

print(my_var_4)
print(my_var_4["day1"])
print(my_var_4["day2"])
