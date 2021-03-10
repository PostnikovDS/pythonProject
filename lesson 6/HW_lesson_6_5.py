# 5.
# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:

    def __init__(self, title):
        self.title = title

    def drew(self):
        print(f'Запуск отрисовки "{self.title}"')


class Pen(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def drew(self):
        print('Запуск отрисовки Pen')


class Pencil(Stationery):

    def __init__(self, title):
        Stationery.__init__(self, title)

    def drew(self):
        print('Запуск отрисовки Pencil')


class Handle(Stationery):

    def drew(self):
        print('Запуск отрисовки Handle')


st = Stationery('некоторая канцелярская принадлежность')
st.drew()

pn = Pen('ручка')
pn.drew()

pl = Pencil('карандаш')
pl.drew()

he = Handle('маркер')
he.drew()
