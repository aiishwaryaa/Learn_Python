# Write a program that take 10 number from user and display which is the largest number.
count = 1
larger = 0
while count <= 10:
    num = int(input(f"Enter a number {count}: "))
    count = count + 1
    if num > larger:
        larger = num
        
print(f"The largest number is {larger}")  
    
#output>>>>>
# Enter a number 1: 1
# Enter a number 2: 2
# Enter a number 3: 3
# Enter a number 4: 4
# Enter a number 5: 5
# Enter a number 6: 6
# Enter a number 7: 7
# Enter a number 8: 8
# Enter a number 9: 9
# Enter a number 10: 999
# The largest number is 999
    