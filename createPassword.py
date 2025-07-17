import random
import string

def createRandomPassword():
    passwordLength = int(input("How many letters should your password have ? "))
    password = ""

    for _ in range(passwordLength):
        randomChar = random.choice(string.ascii_lowercase)
        password += randomChar

    print("your password is: ", password)