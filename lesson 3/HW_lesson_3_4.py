# 4.
# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

num_1 = 0
num_2 = 0


def exponentiation(arg_1, arg_2):
    result = arg_1 ** arg_2
    return result


while not num_1 > 0:
    num_1 = float(input('Введите действительное положительное число: '))

while not num_2 < 0:
    num_2 = int(input('Введите целое отрицательное число: '))

print(exponentiation(num_1, num_2))

print('--------------------------')

num_1 = 0
num_2 = 0


def exponentiation(arg_1, arg_2):
    result = arg_1
    i = 1
    while i < abs(arg_2):
        result = result * arg_1
        i += 1
    return 1 / result


while not num_1 > 0:
    num_1 = float(input('Введите действительное положительное число: '))

while not num_2 < 0:
    num_2 = int(input('Введите целое отрицательное число: '))

print(exponentiation(num_1, num_2))
