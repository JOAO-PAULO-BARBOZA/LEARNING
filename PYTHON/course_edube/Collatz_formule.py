c0 = int(input('Type a natural number: '))
cont = 0
while c0 != 1:
    if c0 % 2 == 0:
        c0 = int(c0/2)
        cont += 1
        print(c0)
    else:
        c0 = 3*c0 + 1
        cont += 1
        print(c0)
print('Steps:', cont)
