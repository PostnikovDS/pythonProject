# 2.
# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректнообработать эту ситуацию
# и не завершиться с ошибкой.

class MyOwnHomeWorkError(Exception):
    def __init__(self, user_txt):
        self.user_txt = user_txt


try:
    num_1 = int(input('введите делимое: '))
    num_2 = int(input('введите делитель: '))
    if num_2 == 0:
        raise MyOwnHomeWorkError('На ноль делить нельзя !!!')
    result = num_1 / num_2

except (MyOwnHomeWorkError, ZeroDivisionError) as err:
    print(err)

except ValueError as err:
    print(err)
    print("Вы ввели не число")

else:
    print(f"Результат деления равен: {result}")


