"""Задача 1.4
Отделение №1 и отделение №2 используют в своей деятельности
препарат лидокаин. Определить через какое время запасы препарата опустеют
на складе, если известно начальное количество препарата S на складе, и,
суточный расход препарата отделениями V1, V2.
Формат входных данных:
    - на вход программы подаются три числа с плавающей точкой S, V1, V2.
Формат выходных данных:
    - приложение должно вывести одно число в соответствии с условием задания.
"""


def get_fp_value(name: str, is_positive: bool = False) -> float:
    """Получение значения величины как числа с плавающей запятой

    Args:
        name (str): Название величины
        is_positive (bool, optional): Число положительное?. По-умолчанию False.

    Raises:
        ValueError: Исключение при попытке ввода не-числа или отрицательного числа (is_positive == True)

    Returns:
        float: число с плавающей запятой
    """
    while True:
        try:
            value = float(input(f"Введите {name}: "))
            if is_positive and value < 0:
                raise ValueError("ОШИБКА: Ожидается неотрицательное число", None)
            return value
        except ValueError as err:
            if len(err.args) == 2:
                print(err.args[0])
            else:
                print("ОШИБКА: Ожидается число")


def get_expenditure_duration(volume: float, vel1: float, vel2: float) -> float:
    """Расчёт времени, в течение которого складские запасы будут исчерпаны

    Args:
        volume (float): Начальный объём препарата
        vel1 (float): Скорость расхода отделением №1
        vel2 (float): Скорость расхода отделением №2

    Raises:
        ValueError: Исключение при попытке ввода отрицательных чисел

    Returns:
        float: Время расхода
    """
    if volume < 0:
        raise ValueError("ОШИБКА: 'volume' должен быть положительный")
    if vel1 < 0:
        raise ValueError("ОШИБКА: 'vel1' должен быть положительный")
    if vel2 < 0:
        raise ValueError("ОШИБКА: 'vel2' должен быть положительный")

    return volume / (vel1 + vel2)


# Названия мер, используемых для решения задачи
names = ["Запасы лидокаина, л", "Расход отделения №1, л/сут", "Расход отделения №2, л/сут"]

# Хранилище значений
measures = dict()

# Ввод параметров
for name in names:
    measures[name] = get_fp_value(name, True)

# Вывод на экран результата расчётов
duration = get_expenditure_duration(measures[names[0]],
                                    measures[names[1]],
                                    measures[names[2]])
print(duration)
