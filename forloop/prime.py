num = int(input("Enter a number: "))
if num < 2:
    print("Not a prime number")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")

# Enter a number: 9
# Not a prime number

# Enter a number: 3
# Prime number