# Criando senha criptografada com Python

# Primeiramente é feito a instalação da biblioteca passlib.
# Em seguida fazemos a importação da biblioteca.

from passlib.hash import pbkdf2_sha256 as cryp


# Aqui criamos uma classe com a senha criptografada, onde round implica na quantidade de cracteres
# embaralhados e salt_size é o tamanho dessa senha. O método verify faz a verificação dessa
# senha.


class Usuario:
    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def verificar_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False


nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')
email = input('Digite seu email: ')
senha = input('Digite uma senha: ')
confirma_senha = input('Confirme sua senha: ')

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
else:
    "As senhas não conferem."
    exit(1)

senha = input('Informe a senha para acesso: ')

if user.verificar_senha(senha):
    print("Acesso permitido.")
else:
    print("Acesso negado.")
print(f"Senha do usuário criptrografada {user._Usuario__senha}")
