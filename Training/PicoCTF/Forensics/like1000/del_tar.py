import os, time

for i in range(999):
    now = 1000-i
    print(f'Now Deleting : {now}.tar')

    os.system(f'rm {now}.tar')

