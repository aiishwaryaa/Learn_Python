import random
import string 

class Password_Generator:
    def __init__(self , length , charAllowed, numAllowed):
        self.length = length
        self.charAllowed = charAllowed
        self.numAllowed = numAllowed

    def Generate_Password(self):
        password = ""
        character = string.ascii_letters 

        if self.charAllowed:
            character += string.punctuation

        if self.numAllowed:
            character += string.digits

        password = "".join(random.choice(character) for _ in range(self.length))
        return password

length = int(input("enter the length : ")) 
numAllowed = input("do you want to include numbers: (yes/no)-->").strip().lower()=="yes"
charAllowed = input("do you want to include special characters: (yes/no)-->").strip().lower()=="yes"

pg = Password_Generator(length ,numAllowed,charAllowed) 
print(f"Generated Password: {pg.Generate_Password()}")

        