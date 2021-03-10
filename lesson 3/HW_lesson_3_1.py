# 1.
# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

try:
    def division(num_1, num_2):
        result = num_1 / num_2
        return result


    user_number_1 = int(input('Введите первое число: '))
    user_number_2 = int(input('Введите второе число число: '))

    print(f"Результат деления {round(division(user_number_1, user_number_2), 2)}")

except ZeroDivisionError:
    print('Попытка деления на "0"')
except Exception:
    print('Неизвестная ошибка')
