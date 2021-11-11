from random import randint
import os

os.chdir("message")

lst = []
for i in range(len(os.listdir())):
    os.chdir(str(i))
    lst.append([0] * len(os.listdir()))
    os.chdir("..")

message = ""

for l in lst:
    x = 0
    while x != len(l):
        x = randint(0, 255)
    
    message += chr(x)

os.system(f'echo {message}')

