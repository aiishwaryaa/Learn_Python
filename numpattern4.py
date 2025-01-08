n = 5 #numbr of rows
i = n #5 4 3 2 1

while i > 0:
    j = i #5 4 3 2 1
    while j <= n :
        print(j, end = " ") 
        j += 1
    print()
    i -= 1 # 4  3  2  1


# output>>>
# 5 
# 4 5
# 3 4 5
# 2 3 4 5
# 1 2 3 4 5