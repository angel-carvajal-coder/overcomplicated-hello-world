import os

os.mkdir("message")
os.chdir("message")

for i, char in enumerate("Hello, World!"):
    os.mkdir(str(i))
    os.chdir(str(i))
    for j in range(ord(char)):
        os.mkdir(str(j))
        os.chdir(str(j))
        open("file", "w").close()
        os.chdir("..")
    os.chdir("..")