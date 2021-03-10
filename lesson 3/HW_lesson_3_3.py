# 3.
# Реализовать функцию my_func(),
# которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(arg_1, arg_2, arg_3):
    args = [arg_1, arg_2, arg_3]
    args.remove(min(args))
    return sum(args)


num_1 = int(input("Введите 1-й аргумент: "))
num_2 = int(input("Введите 2-й аргумент: "))
num_3 = int(input("Введите 3-й аргумент: "))

result = my_func(num_1, num_2, num_3)
print(result)
