"""Para utilizar a função reduce() é necessário importá-lo da biblioteca functools"""

from functools import reduce
print(122*"-")
print("EXEMPLO COM REDUCE")
lista = [1, 2, 3, 4, 5]
print(f'Lista {lista}')

resultado = reduce(lambda x, y: x*y, lista)  # mult. os 2 primeiros da lista, em seguida o res. pelo seguite.

print(f'Resultado {resultado}')
print(122*"-")
print("EXEMPLO COM UM 'FOR'")

res = 1
for i in lista:
    res = res*i

print(f'Lista {lista}')
print(f'Resultado {res}')




