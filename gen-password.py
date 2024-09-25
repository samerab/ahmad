import random

def gen_pass():
    l = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    l8 = random.choices(l,k=8)
    password = ''.join(l8)
    return password

str = ""
for i in range(1,101):
    str += f"{gen_pass()}\n"
with open("passwords.txt","w") as file:
    file.write(str)
