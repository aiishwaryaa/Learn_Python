# Write a program that take 10 number from user and display which is the largest number and which one is the lowest.

count = 1
larger = int(input(f"Enter a number: "))
lower = larger
while count <= 9:
    num = int(input(f"Enter a number {count} : "))
    if num > larger:
        larger = num
    if num < lower:
        lower = num
    count += 1

print(f"The largest number is {larger} and the lowest number is {lower}")  #

