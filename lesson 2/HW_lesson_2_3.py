# 3.
# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

user_month = int(input("Введите номер месяца(1-12) : "))
year_dict = {
    1: 'зима', 2: 'зима', 3: 'весна',
    4: 'весна', 5: 'весна', 6: 'лето',
    7: 'лето', 8: 'лето', 9: 'осень',
    10: 'осень', 11: 'осень', 12: 'зима'
}

for key in year_dict.keys():
    if key == user_month:
        season = year_dict.get(key)
        print(f"Время года вашего месяца : {season}")

# -------------------------------------------

user_month = int(input("Введите номер месяца(1-12) : "))
seasons_list = ['весна', 'лето', 'осень', 'зима']
season = None

if user_month == 3 or user_month == 4 or user_month == 5:
    season = seasons_list[0]
elif user_month == 6 or user_month == 7 or user_month == 8:
    season = seasons_list[1]
elif user_month == 9 or user_month == 10 or user_month == 11:
    season = seasons_list[2]
elif user_month == 12 or user_month == 1 or user_month == 2:
    season = seasons_list[3]

print(f"Время года вашего месяца : {season}")
