s = "Aishwarya Bachchani"
print(s.lower())  # Output: aishwarya bachchani
print(s.title())  # Output: Aishwarya Bachchani
print(s.upper())  # Output: AISHWARYA BACHCHANI

text = "i AM a ProGRAmmER "
print(text.swapcase())  # Output: I am A pROgraMMer

a = "jthjbg43456765  5y bvg"
print(a.isalnum())  # Output: False
print(a.isalpha())  # Output: False

a2 = "jthjbg434567655ybvg"
print(a2.isalnum())  # Output: True
print(a2.isalpha())  # Output: False

s = "123456789"
print(s.isdigit())  # Output: True

s = "its a beautiful day today!"
print(s.split())  # Output: ['its', 'a', 'beautiful', 'day', 'today!']
print(s.split('a'))  # Output: ['its ', ' be', 'utiful d', 'y tod', 'y!']


print("ABCD".rjust(10,"=")) #output: ======ABCD
print("ABCD".ljust(10,"=")) #output: ABCD=====


s = "have a nice day"
print(s.find("nice")) #output: 8

print(s.startswith("h")) #true
print(s.startswith("a")) #false
