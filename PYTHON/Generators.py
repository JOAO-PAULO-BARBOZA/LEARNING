""" Parecido com list comprehensin, Generators Expressions economiza mais espaço em memoria
 e usa '()' ao invés de '[]'.
 """

from sys import getsizeof  # Mostra o tamanhos dos objetos em byte.

print(122*"-")
print('EXEMPLO PARA LISTA')

list_comprehensin = [i**2 for i in range(10) if i > 1]
print(list_comprehensin)
print(type(list_comprehensin))
print(f'Quantidade de bytes em memória {getsizeof(list_comprehensin)}')
print(122*"-")

print('EXEMPLO PARA SET/CONJUNTO')

set_comprehensin = {i**2 for i in range(10) if i > 1}
print(set_comprehensin)  # O set não ordena os números
print(type(set_comprehensin))
print(f'Quantidade de bytes em memória {getsizeof(set_comprehensin)}')

print(122*"-")

print('EXEMPLO PARA DICTONARY')

dict_comprehensin = {i: i**2 for i in range(10) if i > 1}
print(dict_comprehensin)
print(type(dict_comprehensin))
print(f'Quantidade de bytes em memória {getsizeof(dict_comprehensin)}')
print(122*"-")

print('EXEMPLO PARA GENERATORS EXPRESSIONS')

gen = (i**2 for i in range(10) if i > 1)
print(gen)  # O generator não mostra o que foi gerado, apenas a posição em memória
print(type(gen))
print(f'Quantidade de bytes em memória {getsizeof(gen)}')
print(122*"-")
