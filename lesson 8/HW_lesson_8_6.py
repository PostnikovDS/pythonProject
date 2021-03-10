# 6.
# Продолжить работу над вторым заданием.
# Реализуйте механизм валидации вводимых пользователем данных. Например, для указания количества принтеров,
# отправленных на склад, нельзя использовать строковый тип данных.
from time import sleep


class Warehouse:

    @staticmethod
    def goods_receipt(equipment, amount):
        consignment = {equipment: amount}
        return consignment


class OfficeEquipment:

    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity


class Printer(OfficeEquipment):

    def __init__(self, name, quantity, multicolor):
        super().__init__(name, quantity)
        self.multicolor = multicolor

    def print_out(self):
        print('Печать документа')


class Scanner(OfficeEquipment):

    def __init__(self, name, quantity, form):
        super().__init__(name, quantity)
        self.form = form

    def to_scan(self):
        print('Сканирование документа')


class Xerox(OfficeEquipment):

    def __init__(self, name, quantity, price):
        super().__init__(name, quantity)
        self.price = price

    def to_scan(self):
        print('Сканирование документа')


while True:

    try:

        pr = Printer('Принтер', int(input('Введите количество принтеров: ')), True)
        sc = Scanner('Сканер', int(input('Введите количество сканеров: ')), 'Flatbed')
        xr = Xerox('Ксерокс', int(input('Введите количество ксероксов: ')), '48000 руб')

    except ValueError as err:
        print('Вы ввели не число!')

    else:

        consignment_1 = Warehouse.goods_receipt(pr.name, pr.quantity)
        consignment_2 = Warehouse.goods_receipt(sc.name, sc.quantity)
        consignment_3 = Warehouse.goods_receipt(xr.name, xr.quantity)

        sc.to_scan()
        sleep(2)
        pr.print_out()
        sleep(2)

        consignment = {**consignment_1, **consignment_2, **consignment_3}
        print(f'Поступление товара на склад:\n{consignment}')
        break
