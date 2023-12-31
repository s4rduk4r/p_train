"""Задача 1.3
Взрослая поликлиника обслуживает пациентов в возрасте 18-100лет.
Создайте программу, определяющую к какому специалисту урологу или
гинекологу необходимо отправить пациента во время обследования.
Программа должна принимать возраст и пол пациента. Пол обозначения:
m (male – мужчина), f (female – женщина). Если пациент не подходит по
возрасту, то вывести «Пациент не подходит по возрасту». В противном случае
для мужчин вывести: «уролог», а для женщин - «гинеколог».
Формат входных данных:
    - Возраст пациента - натуральное число.
    - Пол пациента – буква, обозначающая пол m (мужчина) или f (женщина).
Формат выходных данных:
    - программа должна вывести текст в соответствии с условиями задания.
"""


def get_age() -> int:
    """Получение возраста из стандартного ввода

    Raises:
        ValueError: ввод не является числом или является отрицательным числом
        
    Returns:
        int: возраст
    """
    while True:
        try:
            _age = int(input("Введите возраст, лет: "))
            if _age < 0:
                # Второй аргумент конструктора передаётся для конкретизации ошибки
                # в обработчике ошибок
                raise ValueError("ОШИБКА: Возраст должен быть положительным числом", None)
            return _age
        except ValueError as err:
            if len(err.args) == 2:
                print(err.args[0])
            else:
                print("ОШИБКА: Ожидается целое число лет")


def get_gender() -> str:
    """Получение пола из стандартного ввода

    Raises:
        ValueError: _description_

    Returns:
        str: _description_
    """
    while True:
        try:
            _gender = input("Введите пол (m - мужской, f - женский): ").lower()
            if _gender in ["m", "f"]:
                return _gender
            raise ValueError()
        except ValueError:
            print("ОШИБКА: Ожидается буква")


def is_valid_age(age: int, lower: int, upper: int) -> bool:
    """Проверка возраста пацинета на соответствие

    Args:
        age (int): возраст
        lower (int): нижний возрастной предел
        upper (int): верхний возрастной предел
        
    Raises:
        ValueError: хотя бы один из аргументов отрицательный

    Returns:
        bool:
            True - возраст находится в заданном диапазоне
            False - возраст находится вне заданного диапазона
    """
    if age < 0:
        raise ValueError("ОШИБКА: 'age' должен быть положительным числом")
    if lower < 0:
        raise ValueError("ОШИБКА: 'lower' должен быть положительным числом")
    if upper < 0:
        raise ValueError("ОШИБКА: 'upper' должен быть положительным числом")
    return lower <= age <= upper


# Получение входных данных
age = get_age()
gender = get_gender()

# Возрастной диапазон
age_bounds = (18, 100)

if is_valid_age(age, age_bounds[0], age_bounds[1]):
    if gender == "m":
        print("уролог")
    else:
        print("гинеколог")
else:
    print("Пациент не подходит по возрасту")
