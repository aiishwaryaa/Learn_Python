n1 = float(input("enter first number:  "))
n2 = float(input("enter second number:  "))
operator = input("enter any operator =>(+,-,*,/,%): ")

if operator == "+":
    result = n1 + n2
elif operator == "-":
    result = n1 - n2
elif operator == "*":
    result = n1 * n2
elif operator == "/":
    if n2 != 0:
        result = n1 / n2
    else:
        result = "Divide by zero error"
elif operator == "%":
    if n2 !=0:
        result = n1 % n2
    else:
        result = "Divide by zero error"
else:
    result = "Invalid operator"

print(f"The result is : {result}")    