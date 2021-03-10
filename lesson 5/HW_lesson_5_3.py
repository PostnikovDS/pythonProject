# 3.
# Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open('text_3.txt', encoding="utf-8") as file:
    poor_staff = []
    list_salary = []
    employees = 0

    for line in file:
        employees += 1
        print(line, end='')
        x = line.split()
        salary = float(x[1])
        list_salary.append(salary)
        if salary < 20000:
            poor_staff.append(x[0])
    print(f'Сотрудники с низкой зарплатой: {poor_staff}')

    general_sum = 0
    for i in list_salary:
        general_sum += i
    average = general_sum / employees
    print(f'Средняя величина дохода сотрудников: {average}')
