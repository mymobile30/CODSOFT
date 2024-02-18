import random
import string
def generate_pass(x):
    char=string.ascii_letters + string.digits + string.punctuation
    password= ''.join(random.choice(char) for i in range(x))
    return password
length=int(input("Enter the length of the password : "))
print("Generate password :",generate_pass(length))
