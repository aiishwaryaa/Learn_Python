# Write a program to take 5 number as input and print which one is positive and which one is negative.
count = 1
while count <= 5:
    num = int(input("Enter a number: "))
    if num > 0:
        print(num, "is a positive number")
    elif num < 0:
        print(num, "is a negative number")
    else:
        print(num, "is zero")

count += 1

#output>>>>
# Enter a number: 2
# 2 is a positive number
# Enter a number: 3
# 3 is a positive number
# Enter a number: 0
# 0 is zero
# Enter a number: -8
# -8 is a negative number
# Enter a number: -0
# 0 is zero
# Enter a number: 38
# 38 is a positive number