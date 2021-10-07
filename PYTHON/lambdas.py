# LAMDAS SÃO FUNÇÕES ANÔNIMAS

""" Nessa expressão x representa o valor e o que vem depois dos ':' é o retorno da função."""
variavel = lambda x: 3 + x + 1

""" Nessa expressão recebemos um nome e um sobrenome e tiremos os espaços vazios do início e final(strip)
e colocamos as iniciais em maiúsculo.
"""
nome_completo = lambda nome, sobrenome: nome.strip().title() + " " + sobrenome.strip().title()
print(nome_completo("  joãO PAulo ", "    BEZERRA"))

""" Nessa expressão organizamor uma lista pelo sobrenome usando o metodo 'sort' com 'key' """

autores = ['H. G. Wells', 'Ray Brodbury', 'Isaac Asimov']
print(autores)
autores.sort(key=lambda sobrenome: sobrenome.split(" ")[-1].lower())
print(autores)

" Função quadratica usando uma lambda"


def funcao_quadrada(a, b, c):
    return lambda x: a * x ** 2 + x * b + c


print(funcao_quadrada(3, 0, 1)(2))
