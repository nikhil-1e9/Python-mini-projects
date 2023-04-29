# Let's generate a random password by creating a simple password generator

import random 

chars = "!@#$%^&*()_+-=`~{}[];:<>,.?/|\1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
L = len(chars)
passlen = int(input("Enter length of password: "))

password = ""
for _ in range(passlen):
    password += random.choice(chars)
    
print("Generated Password:", password)
    
