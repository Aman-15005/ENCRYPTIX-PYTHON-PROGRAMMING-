import random
characters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ/*-+!@#$%&(?)"
b=int(input("enter the length of the password you want"))
password=""
for i in range(b):
    password+=random.choice(characters)
print("Hey ! Your desired  password is \n",password)