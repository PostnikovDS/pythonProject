# 4.
# Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

class Warehouse:
    '''Склад'''


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
