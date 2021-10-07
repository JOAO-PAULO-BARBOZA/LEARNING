from time import sleep
lista = []
cont = 0
while len(lista) < 100:
    lista.append(2**cont)
    cont += 1
    sleep(3)  # Tempo para a adição do novo número em segundos
    print(f'Formação da potcia de 2')
    print(lista)
