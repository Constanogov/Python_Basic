def power_numbers(*number):
    square: list[number] = []
    for el in number:
        square.append(el ** 2)
    return square

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
    if k <= 0 and 1 < num:
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
        return list(filter(filter_odd_num, num))
    elif filter_type == EVEN:
        return list(filter(filter_even_num, num))
    elif filter_type == PRIME:
        return list(filter(is_prime, num))
