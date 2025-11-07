import pandas as pd

# Example Series
s1 = pd.Series([10, 20, 30, 40])
s2 = pd.Series([1, 2, 3, 4])

# Arithmetic operations
add_result = s1 + s2               # or s1.add(s2)
sub_result = s1 - s2               # or s1.sub(s2)
mul_result = s1 * s2               # or s1.mul(s2)
div_result = s1 / s2               # or s1.div(s2)
floordiv_result = s1 // s2         # or s1.floordiv(s2)
mod_result = s1 % s2               # or s1.mod(s2)
pow_result = s1 ** s2              # or s1.pow(s2)

# Print results
print("Addition:\n", add_result)
print("Subtraction:\n", sub_result)
print("Multiplication:\n", mul_result)
print("Division:\n", div_result)
print("Floor Division:\n", floordiv_result)
print("Modulus:\n", mod_result)
print("Power:\n", pow_result)
