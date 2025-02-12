#Dictionaries in Python are mutable, unordered collections of key-value pairs.
#  They are highly efficient for lookups, insertions, and deletions based on unique keys.

# Empty dictionary
my_dict = {}

# Dictionary with values
my_dict = {"name": "Aishwarya", "age": 25, "city": "jaipur"}

# methods:>...

# 1. clear()   >> Removes all items from the dictionary.
my_dict = {"name": "Aishwarya", "age": 25}
my_dict.clear()
print(my_dict)  # Output: {}

# 2.copy() >>>>>>>>> Returns a shallow copy of the dictionary.
my_dict = {"name": "Aishwarya", "age": 25}
new_dict = my_dict.copy()
print(new_dict)  # Output: {'name': 'Aishwarya', 'age': 25}


# 3 fromkeys()  >>Creates a dictionary with specified keys and an optional default value.
keys = ["name","age", "city"]
my_dict = dict.fromkeys(keys,"none")
print(my_dict)  # Output: {'name': 'none', 'age': 'none',}



# 4. get() >>>>>>>>> Returns the value for the given key if it exists in
# the dictionary. If not, it returns the default value.
my_dict = {"name": "Aishwarya", "age": 25}

print(my_dict.get("name"))  # Output: Aishwarya
print(my_dict.get("age"))  # Output: 25



# 5. items() >>Returns a view object of key-value pairs.
my_dict = {"name": "Aishwarya", "age": 25}
print(my_dict.items())
# dict_items([('name', 'Aishwarya'), ('age', 25)])


# 6.keys() >>>Returns a view object of the dictionary's keys.
my_dict = {"name": "Aishwarya", "age": 25}
print(my_dict.keys())
# dict_keys(['name', 'age'])


# 7. pop()
# Removes the item with the specified key and returns its value.
my_dict = {"name": "Aishwarya", "age": 25}
print(my_dict.pop("name"))  # Output: Aishwarya


# 8. popitem()>> Removes and returns the last key-value pair as a tuple.
my_dict = {"name": "Aishwarya", "age": 25}
print(my_dict.popitem())  # Output: ('age', 25)

# 9. setdefault()  >>>  Returns the value of a specified key. If the key does not exist, inserts the key with a specified value.
