string = input("Enter a string: ")
char = input("Enter any character: ")
i = 0

while i < len(string):
    if string[i] == char:
        print(f"The index value of '{char}' is {i}")
        break
    i += 1
else:
    print(f"The character '{char}' is not in the string.")
