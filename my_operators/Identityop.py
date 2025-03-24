# 5. Identity Operators
# These operators are used to compare objects' memory locations.

# `is`	validate of both values are of same data type and are equal
# `is not`	validate of both values are of same data type and are equal
 
print(28 is "hiii")     #False
print(28 is not "hiii")  # True
print(28 is 28)          # True
print(28 is not 28)       # False
print(28 is 28.0)         # False
print(28 is not 28.0)     # True
print(28 is 50)         # False