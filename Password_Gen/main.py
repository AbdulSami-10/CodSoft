# Random Password Generator

import random as rd
import string as sr

while True:
    try:
        length=int(input("Enter the desired length: "))
        if length <=0:
            raise ValueError
        break
    except ValueError:
         print("Invalid Value! Enter only positive numbers")
    
Characters=sr.ascii_letters+sr.digits+sr.punctuation
password=""

for i in range(length):
    password+=rd.choice(Characters)

print(f"Here is your passworf: {password}")