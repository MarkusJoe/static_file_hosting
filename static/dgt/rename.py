import hashlib
import os


files = list(os.listdir('.'))
files.remove('rename.py')

for i in files:
    with open(f'./{i}', 'rb') as fp:
        md5 = hashlib.md5(fp.read()).hexdigest()
    os.rename(i, md5)
    os.system(f'git add {md5}')
    os.system(f'git commit -m "{i}"')
    print(i, md5, "\n")