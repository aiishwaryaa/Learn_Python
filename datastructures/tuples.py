# methods>>>>>>>

# 1. count()
# The count() method returns the number of occurrences of a specified value in the list.

my_tuple = (1,3,4,56,3,45,6,3,1,3,4,5)
print(my_tuple.count(3))  # Output: 4


# index()
# The index() method returns the index of the first occurrence of the specified value.

my_tuple = (10,20,30,40,50,60)
print(my_tuple.index(40))   
# output: 3

# len()
# The len() function returns the number of items in an object.
my_tuple = (10,20,30,40,50,60,70)
print(len(my_tuple))  #7

# concatenation
# The + operator is used to concatenate two tuples.
my_tuple1 = (1,2,3)
my_tuple2 = (4,5,6)
print(my_tuple1 + my_tuple2)  # Output: (1, 2,3,4,5,6)


# repetition

my_tuple = (1,2)
print(my_tuple * 4)
# Output: (1, 2, 1, 2, 1, 2, 1 ,2)

# membership test
# The in operator is used to check if a value is present in the tuple.
my_tuple = (1,2,3,4,5)
print(3 in my_tuple)  # Output: True


#iteration
my_tuple = (1,2,3,4,5)
for i in my_tuple:
    print(i)


# slicing
my_tuple = (1,2,3,4,5)
print(my_tuple[1:3])  # Output: (2, 3)