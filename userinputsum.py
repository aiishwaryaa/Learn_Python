# Write a program that take 10 number from user and print sum of all numbers.

count = 1
sum = 0
while count <= 10:
    num = int(input(f"Enter number {count} : "))
    sum = sum + num
    count = count + 1

print("Sum of all numbers is: ", sum)  # Output: Sum of all numbers is
   
# output>>>>>>
# Enter number 1 : 1
# Enter number 2 : 2
# Enter number 3 : 3
# Enter number 4 : 4
# Enter number 5 : 5
# Enter number 6 : 6
# Enter number 7 : 7
# Enter number 8 : 8
# Enter number 9 : 9
# Enter number 10 : 10
# Sum of all numbers is:  55