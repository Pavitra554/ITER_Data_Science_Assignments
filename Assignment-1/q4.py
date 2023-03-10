import random
import string


def generate(length):
    # string.ascii_letters gives a-zA-Z
    # string.digits gives 0-9
    characters = string.ascii_letters + string.digits
    # print(characters)
    password = ''.join(random.choices(characters, k=length))
    return password


length = int(input("Enter password length: "))
no_of_password = int(input("Enter number of passwords to generate: "))
passwords = [generate(length) for i in range(no_of_password)]
for password in passwords:
    print(password)
