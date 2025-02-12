# Write a program that take to input from user one is a large string and second input has to be a single character we have to find that character inside the given string but we are not allowed to use any of the inbuilt methods of string.
# to = 2

# string = input("Enter the  string: ")
# char_to_find = input("Enter char to find: ")

# using for loop>>>>>>>>>>>
# count = 0
# for i in string:
#     if i == char_to_find:
#         count += 1

# print(f"the character '{char_to_find}' came {count} times.")

# using function>>>>>>>>>>>>>>
string = input("Enter the  string: ")
char_to_find = input("Enter char to find: ")

def find_char(string_given, char):
    count = 0
    for i in string_given:
        if i == char:
           count += 1

    return count      

result = find_char(string , char_to_find) 
print(f"The Character'{char_to_find}' appeer {result} times")


