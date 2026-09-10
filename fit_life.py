# Проект FitLife - MVP версия 1.0
import sys

sys.stdout.reconfigure(encoding="utf-8")

# while True - делает цикл бесконечным
# Про strip я узнал от нейронки, он отрезает все пробелы
# title делает каждую первую букву заглавной (нейронка)
# break завершает цикл
WATER_PER_KG = 30
ML_IN_LITER = 1000

while True:
    user_name = input("Как тебя зовут? ")
    if user_name.strip():
        user_name = user_name.title()
        break
    else:
        print("Имя не может быть пустым. Пожалуйста, введите имя.")

# while True - делает цикл бесконечным
# isdigit я узнал от нейронки, проверяет цифры ли это.
# break завершает цикл
while True:
    user_age = input("Сколько вам лет? ")
    if user_age.isdigit():
        user_age = int(user_age)
        break
    else:
        print("Ошибка! Пожалуйста, введите только цифры (например, 25).")

# while True - делает цикл бесконечным
# except не ломает программу а выводит ошибку
while True:
    user_weight = input("Ваш вес? (в кг) ")
    try:
        user_weight = float(user_weight)
        if user_weight > 0:
            break
        else:
            print("Вес должен быть положительным числом.")
    except ValueError:
        print("Ошибка! Пожалуйста, введите число (например, 70.5).")
while True:
    user_height = input("Ваш рост? (в м.) ")
    try:
        user_height = float(user_height)
        if 0 < user_height < 3:
            break
        else:
            print("Рост должен быть реалистичным числом (например, 1.75).")
    except ValueError:
        print("Ошибка! Введите корректное число.")

bmi = round(user_weight / (user_height ** 2), 1)
# расчет ИМТ я посмотрел в нейронке
if bmi < 18.5:
    bmi_comment = "Недостаток веса"
elif bmi < 25:
    bmi_comment = "Норма"
elif bmi < 30:
    bmi_comment = "Избыточный вес"
else:
    bmi_comment = "Ожирение"

water_needed = round((user_weight * WATER_PER_KG) / ML_IN_LITER, 1)

print(f"Привет, {user_name}! Я FitLife, давай начнём!")
print(f"ваш возраст: {user_age} лет")
print(f"ваш ИМТ: {bmi} - {bmi_comment}")
print(f"норма воды: {water_needed} мл.")
print("Расчёт окончен. Будьте здоровы!")
