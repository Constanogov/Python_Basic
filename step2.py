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


print(list(filter_numbers([1, 2, 3, 4, 2, 3, 67, 15, 10, 8, 9, 11], PRIME)))
