# Write a program that take 10 number from user and display which is the largest number.
count = 1
larger = int(input(f"Enter a number : "))
while count <= 2:
    num = int(input(f"Enter a number {count}: "))
    count = count + 1
    if num > larger:
        larger = num
        
print(f"The largest number is {larger}")  
    
