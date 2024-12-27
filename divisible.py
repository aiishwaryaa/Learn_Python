n = int(input ("enter a number:  "))

if n % 3 == 0 and n % 5 == 0:
    print("the number is divisible by both")
elif n % 5 == 0:
    print("the number is divisible by 5")
elif n % 3 == 0:
    print("the number is divisible by 3")
else:
    print("the number is not divisible by 3 and 5")