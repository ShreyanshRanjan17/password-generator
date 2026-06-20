import random
import string

length = int(input("Enter password length (more than 10): "))

if length <= 10:
    print("Password should be more than 10 characters.")
else:
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("Generated Password:", password)