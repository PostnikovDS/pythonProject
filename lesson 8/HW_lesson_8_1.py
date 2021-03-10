# 1.
# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц,
# год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.


class Date:
    def __init__(self, user_date):
        self.user_date = user_date

    @classmethod
    def get_date(cls):
        cls.user_date = gd.user_date.split('-')
        # print(cls.user_date)
        for el in cls.user_date:
            el = int(el)
        return cls.user_date

    @staticmethod
    def validation(date):
        day, mounth, year = date
        # print(day, mounth, year)
        error = False
        if 0 < int(day) < 32:
            pass
        else:
            print('дни месяца не могут выходить за диапазон 1-31 !!!')
            error = True

        if 0 < int(mounth) < 13:
            pass
        else:
            print('месяц не может выходить за диапазон 1-12 !!!')
            error = True

        if 1900 < int(year) < 2021:
            pass
        else:
            print('год не может превышать 2021-й и быть меньше 1900-го !!!')
            error = True

        # print(error)

        if error:
            print('Дата введена некорректно')
        else:
            print('Дата введена корректно')


# gd = Date('30-05-1995')
while True:
    try:
        gd = Date(input('Введите дату в формате «день-месяц-год»: '))
        print(gd.get_date())
        Date.validation(gd.get_date())
        break

    except ValueError as err:
        print(err)
        print('Дата введена в неправильном формате. Попробуйте ещё раз.')


