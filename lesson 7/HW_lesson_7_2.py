# 2.
# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class AbstractClothes(ABC):

    @abstractmethod
    def coat_size(self):
        pass

    @abstractmethod
    def suit_growth(self):
        pass


class Clothes(AbstractClothes):

    def __init__(self, name, param):
        self.name = name
        self.param = param

    @property
    def coat_size(self):
        return round((self.param / 6.5 + 0.5), 2)

    @property
    def suit_growth(self):
        return round((2 * self.param + 0.3), 2)

    def __add__(self, other):
        return coat.coat_size + suit.suit_growth


coat = Clothes('пальто', 1000)
print(f'расход ткани для {coat.name} {coat.coat_size}')

suit = Clothes('костюм', 190)
print(f'расход ткани для {suit.name} {suit.suit_growth}')

print(f'общий подсчет расхода ткани', coat + suit)
