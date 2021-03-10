# 7.
# Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта,
# создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class Complex:

    def __init__(self, complex_number):
        self.complex_number = complex_number

    def __str__(self):
        return f"{self.complex_number}"

    def __add__(self, other):
        return Complex(self.complex_number + other.complex_number)

    def __mul__(self, other):
        return Complex(self.complex_number * other.complex_number)

    # def __round__(self, n=2):
    # return не знаю, как округлить количество знаков внутри комплексного числа


complex_1 = Complex(complex(8 + 3j))
complex_2 = Complex(complex(4.3 - 5j))
complex_3 = Complex(complex(11 + 7j))

complex_sum = complex_1 + complex_2 + complex_3
print(f'Результат сложения комплексных чисел: {complex_sum}')
print(type(complex_sum))

complex_mul = complex_1 * complex_2 * complex_3
print(f'Результат умножения комплексных чисел: {complex_mul}')
print(type(complex_mul))

