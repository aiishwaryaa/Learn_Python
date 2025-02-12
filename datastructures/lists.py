a = ["a", 45 , 6.78,"ball", 56778, 42]
a.append("hello")
print(a)
# Output: ['a', 45, 6.78, 'ball', 56778, 42, 'hello']


a.insert(2 , 3)
print(a)
# output : ['a', 45, 3, 6.78, 'ball', 56778, 42, 'hello'] 

print(a.count(45)) #1

a.remove("hello")
print(a)
# output: ['a', 45, 3, 6.78, 'ball', 56778, 42]

a.reverse()
print(a)
# output: [42, 56778, 'ball', 6.78, 3, 45, 'a']

b = ["hii","b",77]
a.append(b)
print(a)
# output: [42, 56778, 'ball', 6.78, 3, 45, 'a', ['hii', 'b', 77]]


a.extend(b)
print(a)
# output: [42, 56778, 'ball', 6.78, 3, 45, 'a', ['hii', 'b', 77], 'hii', 'b', 77]

a.remove(b)
print(a)
# output: [42, 56778, 'ball', 6.78, 3, 45, 'a', 'hii', 'b', 77]


c = [23,45,67,8876,2,1,345,67,0,7]
c.sort()
print(c)
# output: [0, 1, 2, 7, 23, 45, 67, 67, 345, 8876]


print(c.pop())
# output: [0, 1, 2, 7, 23, 45, 67, 67, 345, 8876]
# 8876
print(c.pop(0))
