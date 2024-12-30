# Write a program to take 5 number as input and print which one is positive and which one is negative.
num = 1
while num <= 5:
    Number = int(input("Enter a Number: "))
    if Number > 0:
        print(Number, "is a positive Number")
    elif Number < 0:
        print(Number, "is a negative Number")
    else:
        print(Number, "is zero")

    num += 1

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
