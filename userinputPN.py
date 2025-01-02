# Write a program that take 10 number from user and count how many number are +ve and how many number are -ve.

count = 1
pos_num = 0
neg_num = 0
while count <= 10:
    num = int(input(f"Enter number {count} : "))
    if num > 0:
        pos_num += 1
    elif num < 0:
        neg_num += 1
    else :
        print("Zero is neither +ve nor -ve")
    count += 1
            
print(f"Number of +ve number : {pos_num}")
print(f"Number of -ve number : {neg_num}")


# output>>
# Enter number 1 : 23
# Enter number 2 : -4
# Enter number 3 : -56
# Enter number 4 : -689
# Enter number 5 : 0
# Zero is neither +ve nor -ve
# Enter number 6 : 4222
# Enter number 7 : 45
# Enter number 8 : 67
# Enter number 9 : 32
# Enter number 10 : -9
# Number of +ve number : 5
# Number of -ve number : 4