sales = float(input("enter the total amount of sales : "))

basic = 3000  # Basic salary
hra = 0.2 * basic  # HRA ka calculation (20% of Basic)
da = 1.1 * basic  # DA ka calculation (110% of Basic)
conveyance = 500  # conveyance allowance
bonus = 500  # bonus

if sales > 100000:
    incentive = 0.1 * sales  # incentive = 10% of sales (10/100)
else:
    incentive = 0.05 * sales  # incentive = 5% of sales(5/100)

salary = basic + hra + da + conveyance + incentive + bonus
print(f"Total salary is : Rs.{salary}")