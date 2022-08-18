from random import choice
from time import sleep
lista = ['a', 1, 2, 3, 4, 0]

while True:
    escolha = choice(lista)
    try:
        resultado = 100/escolha
        print(f'A escolha foi {escolha} e o resultado foi {resultado}')
        sleep(3)
    except TypeError:
        print('Sorteu o "a"')
        continue
    except ZeroDivisionError:
        print('Encontrou uma divisão por zero')
        break


    
