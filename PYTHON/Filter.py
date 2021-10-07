"""Filtramos valores para função, onde o filter recebe dois parametros, uma função e um iteravel.
No explemplo foi usado uma expressão lambda.
"""
import statistics

print("EXEMPLO 1")
notas = [5, 8, 7, 10, 8.5, 9.1]

resul = tuple(filter(lambda nota: nota > statistics.mean(notas), notas))

print(resul)  # Primeiro uso

print(resul)  # Mesmo após o primeiro uso não é zerado pois foi usado uma lambda como parametro do filter.

# Exemplo com uma função
print("EXEMPLO 2")
media = statistics.mean(notas)
print(f"Notas {notas}")
print(f"Media das notas {media}")


def maiores_que_a_media(nota):
    return nota > media


resultado = (filter(maiores_que_a_media, notas))
print(f'Acima da média {list(resultado)}')  # Usado a primeira vez
print(list(resultado))  # Após ser usado, o filter zera a lista.

""" Utilizando filter para filtrar listas com espaços vazios"""

print('EXEMPLO 3')

cidades = ['Parelhas', 'Equador', 'Patos', '', '', 'Caicó', '']
print(list(filter(None, cidades)))

print('EXEMPLO 4')
print(list(filter(lambda x: len(x) > 0, cidades)))
