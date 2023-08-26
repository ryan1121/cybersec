import os, time

for i in range(1000):
    now = 1000-i
    print(f'Now : {now}.tar')

    os.system(f'tar -xf {now}.tar')

