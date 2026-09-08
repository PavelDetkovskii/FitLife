# Проект FitLife - MVP версия 1.0
import sys

sys.stdout.reconfigure(encoding="utf-8")

user_name = input("Как тебя зовут? ")

user_age = input("Сколько вам лет? ")
user_age = int(user_age)

user_weight = input("Ваш вес? (в кг) ")
user_weight = float(user_weight)

user_height = input("Ваш рост? (в м.) ")
user_height = float(user_height)

bmi = round(user_weight / (user_height ** 2), 1)

water_needed = round((user_weight * 30) / 1000, 1)

print(f"Привет, {user_name}! Я FitLife, давай начнём!")

print(f"ваш возраст: {user_age} лет, ваш ИМТ: {bmi}, норма воды: {water_needed} мл.")
print("Расчёт окончен. Будьте здоровы!")
