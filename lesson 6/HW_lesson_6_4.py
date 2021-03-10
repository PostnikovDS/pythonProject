# 4.
# Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:

    def __init__(self, name, speed, color, is_police):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        print(f'Go {self.name}!')

    def stop(self):
        print(f'Stop {self.name}!')

    def turn(self):
        print(f'Turn {self.name}!')

    def show_speed(self):
        print(f'{self.speed} км/ч')


class TownCar(Car):

    def __init__(self, name, speed, color, is_police):
        Car.__init__(self, name, speed, color, is_police)

    def show_speed(self):
        if self.speed > 60:
            print('Превышение скорости!')
        else:
            print(f'{self.speed} км/ч')


class SportCar(Car):

    def __init__(self, name, speed, color, is_police):
        Car.__init__(self, name, speed, color, is_police)


class WorkCar(Car):

    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)

    def show_speed(self):
        if wc.speed > 40:
            print('Превышение скорости!')
        else:
            print(f'{self.speed} км/ч')


class PoliceCar(Car):

    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)


c = Car('toyota', 110, 'green', False)
c.go()
c.stop()
c.turn()
c.show_speed()

print('------------------------------')

tc = TownCar('ford', 90, 'blue', False)
tc.go()
tc.stop()
tc.turn()
tc.show_speed()

print('------------------------------')

wc = WorkCar('volkswagen', 50, 'black', False)
wc.go()
wc.stop()
wc.turn()
wc.show_speed()

print('------------------------------')

pc = PoliceCar('BMW', 60, 'white', True)
pc.go()
pc.stop()
pc.turn()
pc.show_speed()

print('------------------------------')

sc = SportCar('ferrari', 180, 'red', False)
sc.go()
sc.stop()
sc.turn()
sc.show_speed()
