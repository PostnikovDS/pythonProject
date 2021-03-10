# 5.
# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

result = 0


def my_func(some_arg):
    summ = 0
    for el in range(len(some_arg)):
        summ = summ + int(some_arg[el])

    global result
    result = summ + result
    print(f'{summ}({result})')


while True:
    numbers = input("Вводите числа через пробел, для завершения программы нажмите 'q' : ").split()

    if 'q' in numbers:
        numbers.remove('q')
        my_func(numbers)
        break

    else:
        my_func(numbers)

print('Программа завершена')
