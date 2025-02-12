string = input("enter a string : ")
i = 0
vowels = "aeiouAEIOU"
while i < len(string):
    print(string[i])
    if string[i] in vowels:
        print("vowel")
    else:
        print("consonant")
    i = i + 1