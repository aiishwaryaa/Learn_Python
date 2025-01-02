# Write a program that take 10 number from user and display which is the largest number and which one is the lowest.

count = 1
larger = 0 
lower = 0
while count <= 10:
    num = int(input(f"Enter a number {count} : "))
    if num > larger:
        larger = num
    if num < lower:
        lower = num
    count += 1

print(f"The largest number is {larger} and the lowest number is {lower}")  #

# output>>>>>
# Enter a number 1 : 3
# Enter a number 2 : 4
# Enter a number 3 : 67
# Enter a number 4 : 890
# Enter a number 5 : 2
# Enter a number 6 : 3
# Enter a number 7 : 45678
# Enter a number 8 : 90987654
# Enter a number 9 : 78900
# Enter a number 10 : 0
# The largest number is 90987654 and the lowest number is 0
