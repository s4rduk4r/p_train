"""Задача 1.2
Написать программу, которая считывает с клавиатуры две строки – имя и фамилию лечащего врача и выводит фразу:
"Здравствуйте, [имя] [фамилия]! Вы только что успешно создали программу на Python."

Удостоверьтесь, что если фамилия не была введена, то восклицательный знак стоит впритык к имени.

Формат входных данных:
    - на вход программы подаются две строки имя и фамилия
Формат выходных данных:
    - программа должна вывести текст согласно условию задачи.
"""

# Ввод данных от пользователя
first_name = input("Введите имя: ")
last_name = input("Введите фамилию: ")

# Шаблон сообщения
msg = f"Здравствуйте, {first_name} {last_name}! Вы только что успешно создали программу на Python."

# Конструктор сообщения
if len(first_name) == 0 and len(last_name) == 0:
    msg = msg.replace(f", {first_name} {last_name}", "")

elif len(last_name) == 0:
    msg = msg.replace(f", {first_name} {last_name}", f", {first_name}")

elif len(first_name) == 0:
    msg = msg.replace(f", {first_name} {last_name}", f", {last_name}")


# Вывод приветствия на экран
print(msg)
