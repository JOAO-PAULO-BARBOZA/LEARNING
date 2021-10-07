"""
Em python as classes começam com a palavra reservada 'class'. Classe é a representação de um objeto
do mundo real computacionalmente.
As classes possuem -> atributos(características), métodos(funções) e construtores.
----- Métodos são funções de uma classe _____________________________
----- Atributos podem ser de instância, de classe ou dinâmicos ------
--> O método construtor é usado atributos de instância, ou seja, é individual pra cada objeto.
--> Atributos de classe é compartilhado com todos os objetos.
--> Atributos dinâmicos são criados em tempo de execução, portanto pertence apenas
ao objeto que o criou.
"""


# Declaração de uma classe exemplo 1


class Carro:  # A classe tem que ser definida com a 1° letra maiúscula ou camel case se for nome composto
    pass  # Essa classe até então não faz nada.


# Instaciamento de um objeto

fiat = Carro()
print(fiat)  # fiat agora é um objeto do tipo carro
print(type(fiat))  # tipo do objeto


# Declaração de uma classe com atributos públicos exemplo 2.


class Pessoa:
    def __init__(self, nome, idade):  # __init__ é o método construtor da classe, equivale a Pessoa().
        self.nome = nome  # atributo da classe
        self.idade = idade  # atributo da classe


# Declaração de uma classe com atributos privados exemplo 3.


class Acesso:
    def __init__(self, email, senha):
        self.__email = email  # O '__' no início caracteriza atributo privado
        self.__senha = senha  # O '__' támbem é conhecido como 'Name Mangling' ou 'duplo underscore'.


# instaciando um objeto e acessando seus atributos


usuario = Acesso('jamesbond@gmail.com', '007')

try:
    print(usuario.__email)  # -> dessa forma não é possivel fazer acesso, pois o atributo é privado.
except AttributeError:
    print('Esse é um atributo privado')

# Outra forma de acessar


print(dir(usuario))  # aqui mostra que podemos acessar pelo Name Mangling '_Acesso__email'.
print(usuario._Acesso__email)
print(usuario._Acesso__senha)


# Declarando outra classe exemplo 4


class Produto:
    imposto = 0.98  # Atributo de classe: 2% de imposto
    contador = 0

    def __init__(self, nome, tipo, preco):
        self.id = Produto.contador + 1  # Forma de gerar id pra cada produto instanciado
        self.nome = nome
        self.tipo = tipo
        self.preco = preco*Produto.imposto
        Produto.contador = self.id

    def desconto(self, porcentagem):  # Criação de um método
        return self.preco*(1 - porcentagem / 100)


# Instanciando objetos
prod1 = Produto('Xbox', 'console', 2500)
prod2 = Produto('sansumg glaxy', 'celular', 1500)
prod1.estrelas = '5'  # Criação de um atributo dinâmico

print(prod1.preco, prod1.id, prod1.estrelas)
print(prod2.preco, prod2.id)

print(prod1.__dict__)  # Acessando os atributos em forma de dicionário

del prod1.estrelas  # Deletando qualquer atributo

print(prod1.__dict__)

print(prod1.desconto(50))  # Chamando o método da classe Produto
