# 5.
# Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру, например словарь.

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


class Scanner(OfficeEquipment):

    def __init__(self, name, quantity, form):
        super().__init__(name, quantity)
        self.form = form


class Xerox(OfficeEquipment):

    def __init__(self, name, quantity, price):
        super().__init__(name, quantity)
        self.price = price


pr = Printer('Принтер', '100 шт', True)
sc = Scanner('Сканер', '80 шт', 'Flatbed')
xr = Xerox('Ксерокс', '50 шт', '48000 руб')

consignment_1 = Warehouse.goods_receipt(pr.name, pr.quantity)
consignment_2 = Warehouse.goods_receipt(sc.name, sc.quantity)
consignment_3 = Warehouse.goods_receipt(xr.name, xr.quantity)

consignment = {**consignment_1, **consignment_2, **consignment_3}
print(f'Поступление товара на склад:\n{consignment}')
