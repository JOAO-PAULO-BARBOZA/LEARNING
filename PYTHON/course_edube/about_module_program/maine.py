"""Para que eu possa importar algum módulo de um lugar que não seja o mesmo que está
o arquivo maine.py (que nesse caso está na pasta 'about_module_program') é nessessário indicar
seu caminho incluindo-o na lista 'path' que foi importada do módulo 'sys'.
"""
from sys import path

path.append("/home/j-paulo/PycharmProjects/Estudos/course_edube/")
# Nota importante: A importação pode ser mesmo se 'my_modules' fosse zip
# Nesse caso my_modules.zip --> my_modules
# O caminho ficaria:("/home/j-paulo/PycharmProjects/Estudos/course_edube/my_modules.zip")
from my_modules.outhers.qualquer_coisa import funcao_inutil
from my_modules.utilities.imc import imc

o_que_eh_isso = funcao_inutil()

imc = imc(1.74, 74)

print(imc)
print(o_que_eh_isso)

"""Também é importate salientar que as pastas são packges, onde 'my_modules' é o packge principal
então como ele é a raiz do caminho, tem que ser criado um arquivo '__init__.py' nele para que o 
python saiba onde começar a busca.
"""
