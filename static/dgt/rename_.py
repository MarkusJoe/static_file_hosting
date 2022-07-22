import os


files = list(os.listdir("./"))
files.remove("rename_.py")
files.remove("rename.py")

for i in files:
    os.rename(i, i + ".png")
