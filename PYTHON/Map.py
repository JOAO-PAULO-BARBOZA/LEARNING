"""Mapeamos valores para função, onde o map recebe dois parametros, uma função e um iteravel.
No explemplo foi usado uma expressão lambda.
"""
import math
print("EXEMPLO 1")
raios = [3, 8, 7]

areas2 = tuple(map(lambda raio: math.pi + (raio ** 2), raios))
print(areas2)
print(areas2)

# Exemplo com uma função
print("EXEMPLO 2")


def areas(r):
    return math.pi + (r ** 2)


resultado = (map(areas, raios))
print(list(resultado))  # Usado a primeira vez
print(list(resultado))  # Após ser usado, o map zera a lista.
