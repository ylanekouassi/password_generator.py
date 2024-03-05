#PASSWORD GENERATOR

import random, string

password = int(input("Password's Length: "))
new_password =""

for i in range(password):
    new_password += random.choice(string.ascii_letters)

print(new_password)
