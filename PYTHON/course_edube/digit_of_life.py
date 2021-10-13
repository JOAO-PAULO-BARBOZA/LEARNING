"""Faz a soma de todos os dígitos até restar apenas um digito."""
date = input("Type your birthday date: ")

total = 0
while len(date) != 1:
    for i in date:
        total = total + int(i)
    date = str(total)
    total = 0
print(date)