#3. Logical Operators
#These operators are used to combine conditional statements.

#`and`	Logical AND	True and False results in False
#`or`	Logical OR	True or False results in True
#`not`	Logical NOT	not True results in False


##  and operator rules

#* If both values are True then it will pick the one on Right
#* If Any value is False it will pick the False value

## or operator

#* If both the values are True It will pick the one on Left
#* If any of the value is True it will pick the True one
#* If both the value are False then it will pick the Right side value


print(34 and 45) #45  dono true hai to  right wala value ayega
print(34 and 0)  #0   ek bhi false hai to false value ayegi
print(0 and 45)  #0   ek bhi false hai to false value ayegi
print(0 and 0)   #0   dono false hai to false return ayega

print(34 or 45)  #34 dono true h to left wali val ayegi
print(34 or 0)   #34 koi ek true h to true wali value ayegi
print(0 or 45)   #45 koi ek true h to true wali value ayegi
print(0 or 0)    #0  dono false hai to false 
print(0 or 0 or 0 or 0 or 0) #0 all false 

print(not 34) #False opposite krdega

print(34 and 45 or 2 and 58 and 0 or 50) #45
# 0 or 50 => 50
# 58 and 50 => 50
# 2 and 50 => 50
# 45 or 50 => 45
# 34 and 45 => 45

print(not 67 or 0 and 5 or 67 and 35) #False
#67 and 35 => 35
#5 or 35 => 5
#0 and 5 => 0
#67 or 0 => 67
#not 67 => False
