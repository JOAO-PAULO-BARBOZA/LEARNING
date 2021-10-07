def f(x):
    if x == 0:
        return 0
    return x + f(x - 1)


print(f(2))


# FATORIAL

def fatorial(number):
    if number == 1:
        return 1
    return number * fatorial(number - 1)


print(fatorial(5))
