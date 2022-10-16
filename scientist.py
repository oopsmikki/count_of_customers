
# 1. Фунция, для подсчёта групп, когда нумерации ID начинается с 0.

def count_of_customers(n_customers):
    groups = {}    # Создаём словарь, в котором будем считать кол-во покупателей в каждой группе.
    for id in range(0, n_customers):
        suma = 0
        while id > 0:
            digit = id % 10
            suma += digit
            id = id // 10    # Вычисляем сумму цифр в каждом ID.
        if suma in groups:
            groups[suma] += 1
        else:
            groups[suma] = 1    # Группируем в словарь.
    return print(groups)

# 2. Фунция, для подсчёта групп, когда нумерации ID начинается с произвольного числа.

def count_of_customers(n_customers, n_first_id):
    groups = {}    # Создаём словарь, в котором будем считать кол-во покупателей в каждой группе.
    for i in range(0, n_customers):
        id = n_first_id + i
        suma = 0
        while id > 0:
            digit = id % 10
            suma += digit
            id = id // 10    # Вычисляем сумму цифр в каждом ID.
        if suma in groups:
            groups[suma] += 1
        else:
            groups[suma] = 1    # Группируем в словарь.
    return print(groups)