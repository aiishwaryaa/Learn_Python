# Write a program that take a number as input and print it's table.

num = int(input("enter a number to print its table: "))
counter = 1
while counter <= 10:
    print(f"{num} * {counter} = {num * counter}")
    counter +=1

    #output>>>

# enter a number to print its table: 5
# 5 * 1 = 5
# 5 * 2 = 10
# 5 * 3 = 15
# 5 * 4 = 20
# 5 * 5 = 25
# 5 * 6 = 30
# 5 * 7 = 35
# 5 * 8 = 40
# 5 * 9 = 45
# 5 * 10 = 50