# 5.
# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

income = int(input('Введите выручку фирмы: '))
costs = int(input('Введите издержки фирмы: '))

if income > costs:

    profit = income - costs
    print('Ваша фирма получила прибыль:', profit, 'руб.')
    profitability = round((profit / income * 100), 2)
    print(f'Рентабельность фирмы равна:, {profitability}%')
    employees_count = int(input('Сколько сотрудников в вашей фирме? : '))
    profit_on_employee = round((profit / employees_count), 2)
    print('Прибыль в расчёте на одного сотрудника равна: ', profit_on_employee, 'руб.')

elif income == costs:

    print('Ваша фирма не получила прибыль и не несёт убыток')

elif income < costs:

    lesion = costs - income
    print('Ваша фирма несёт убыток: ', lesion, ' руб.')


# ------------------------------

income = int(input('Введите выручку фирмы: '))
costs = int(input('Введите издержки фирмы: '))

if income > costs:

    profit = income - costs
    print('Ваша фирма получила прибыль:', profit, 'руб.')
    profitability = profit / income * 100
    print('Рентабельность фирмы равна:, {:.2f}%'.format(profitability))
    employees_count = int(input('Сколько сотрудников в вашей фирме? : '))
    profit_on_employee = profit / employees_count
    print('Прибыль в расчёте на одного сотрудника равна: {:.2f} руб'.format(profit_on_employee))

elif income == costs:

    print('Ваша фирма не получила прибыль и не несёт убыток')

elif income < costs:

    lesion = costs - income
    print('Ваша фирма несёт убыток: ', lesion, ' руб.')