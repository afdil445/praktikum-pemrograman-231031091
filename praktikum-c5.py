import os
os.system('clear')

a = True
Limit = 5
i = 0

while a:
    i += 1
    print(f'Menjalankan program {Limit + - i}')
    if i == Limit:
        a = False
        print('program behenti di sini')
    else:
        a = True