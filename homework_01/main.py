"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*number):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    square: list[Any] = []
    for el in number:
        square.append(el**2)
    return square


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers():
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


# Простые
def is_prime(num):
    k = 0
    for i in range(2, num):
        if 0 == num % i:
            k = k + 1
    if k <= 0 and num != 1:
        return True
    else:
        return False


# Не чётные
def filter_odd_num(num):
    if (num % 2) != 0:
        return True
    else:
        return False


# Четные
def filter_even_num(num):
    if (num % 2) == 0:
        return True
    else:
        return False


def filter_numbers(num, filter_type):
    if filter_type == ODD:
        return filter(filter_odd_num, num)
    elif filter_type == EVEN:
        return filter(filter_even_num, num)
    elif filter_type == PRIME:
        return filter(is_prime, num)

