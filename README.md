# Lab-13
Лабораторна робота 13: Робота з різними алгоритмами у Python

Мета цієї лабораторної роботи - навчитися реалізовувати та використовувати різноманітні алгоритми у Python для роботи з числовими даними, обробки рядків, матриць та виконання інших операцій. Завдання включають інтерполяцію пропущених значень, генерацію чисел Фібоначчі, обробку пакетів даних, кодування та декодування рядків, обертання матриць, пошук за регулярними виразами, злиття відсортованих масивів, перевірку на прості числа, групування даних за ключем та видалення аномальних значень.

Опис завдання:

Інтерполяція пропущених значень у списку:
def interpolate_missing(numbers):
    interpolated = []
    for i, num in enumerate(numbers):
        if num is None:
            left = next((n for n in reversed(numbers[:i]) if n is not None), None)
            right = next((n for n in numbers[i+1:] if n is not None), None)
            if left is not None and right is not None:
                interpolated_num = (left + right) / 2
            elif left is not None:
                interpolated_num = left
            elif right is not None:
                interpolated_num = right
            else:
                interpolated_num = 0
            interpolated.append(interpolated_num)
        else:
            interpolated.append(num)
    return interpolated

# Приклад використання
print(interpolate_missing([1, None, 3, None, 5]))  # Виведе: [1, 2.0, 3, 4.0, 5]

Генерація чисел Фібоначчі:
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Приклад використання
print(list(fibonacci(10)))  # Виведе: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

Обробка пакетів даних:
def process_batches(numbers, batch_size):
    max_values = []
    for i in range(0, len(numbers), batch_size):
        batch = numbers[i:i+batch_size]
        max_values.append(max(batch))
    return max_values

# Приклад використання
print(process_batches([1, 3, 5, 2, 8, 6, 7, 4], 3))  # Виведе: [5, 8, 7]

Кодування та декодування рядків:
def encode_string(string):
    encoded = ""
    count = 1
    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            count += 1
        else:
            encoded += str(count) + string[i - 1]
            count = 1
    encoded += str(count) + string[-1]
    return encoded

def decode_string(encoded):
    decoded = ""
    i = 0
    while i < len(encoded):
        count = int(encoded[i])
        char = encoded[i + 1]
        decoded += char * count
        i += 2
    return decoded

# Приклад використання
encoded = encode_string("aaabbc")
print(encoded)  # Виведе: 3a2b1c
print(decode_string(encoded))  # Виведе: aaabbc

Обертання матриці:
def rotate_matrix(matrix):
    n = len(matrix)
    rotated = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated[j][n - i - 1] = matrix[i][j]
    return rotated

# Приклад використання
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(rotate_matrix(matrix))
# Виведе:
# [[7, 4, 1],
#  [8, 5, 2],
#  [9, 6, 3]]

Пошук за регулярними виразами:
import re
def regex_search(strings, pattern):
    return [string for string in strings if re.search(pattern, string)]

# Приклад використання
print(regex_search(["apple", "banana", "cherry"], r'a.+e'))  # Виведе: ['apple']

Злиття двох відсортованих масивів:
def merge_sorted_arrays(arr1, arr2):
    merged = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    merged.extend(arr1[i:])
    merged.extend(arr2[j:])
    return merged

# Приклад використання
print(merge_sorted_arrays([1, 3, 5], [2, 4, 6]))  # Виведе: [1, 2, 3, 4, 5, 6]

Перевірка на прості числа:
import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# Приклад використання
print(is_prime(29))  # Виведе: True
print(is_prime(30))  # Виведе: False

Групування даних за ключем:
def group_by_key(data, key):
    grouped = {}
    for item in data:
        grouped.setdefault(item[key], []).append(item['value'])
    return grouped

# Приклад використання
data = [{'key': 'a', 'value': 1}, {'key': 'b', 'value': 2}, {'key': 'a', 'value': 3}]
print(group_by_key(data, 'key'))  # Виведе: {'a': [1, 3], 'b': [2]}

Видалення аномальних значень:
import math

def remove_outliers(numbers):
    mean = sum(numbers) / len(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    std_deviation = math.sqrt(variance)
    return [x for x in numbers if abs(x - mean) <= 2 * std_deviation]

# Приклад використання
print(remove_outliers([10, 12, 23, 23, 16, 23, 21, 16, 50, 55, 22, 21, 14, 17, 22, 20, 19, 15, 25, 18]))
# Виведе: [10, 12, 23, 23, 16, 23, 21, 16, 22, 21, 14, 17, 22, 20, 19, 15, 25, 18]

Виконання роботи:
Інтерполяція пропущених значень: Реалізовано функцію для заміни None на середнє значення сусідніх чисел.
Генерація чисел Фібоначчі: Реалізовано генератор, який генерує числа Фібоначчі.
Обробка пакетів даних: Реалізовано функцію для обробки чисел у пакетах заданого розміру та знаходження максимального значення в кожному пакеті.
Кодування та декодування рядків: Реалізовано функції для кодування рядків у формат count + character та декодування їх.
Обертання матриці: Реалізовано функцію для обертання квадратної матриці на 90 градусів вправо.
Пошук за регулярними виразами: Реалізовано функцію для пошуку рядків, що відповідають заданому шаблону.
Злиття двох відсортованих масивів: Реалізовано функцію для злиття двох відсортованих масивів в один.
Перевірка на прості числа: Реалізовано функцію для перевірки, чи є число простим.
Групування даних за ключем: Реалізовано функцію для групування словників за заданим ключем.
Видалення аномальних значень: Реалізовано функцію для видалення значень, які є аномальними (виходять за межі двох стандартних відхилень від середнього).
Результати:

Інтерполяція пропущених значень: [1, 2.0, 3, 4.0, 5]
Генерація чисел Фібоначчі: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
Обробка пакетів даних: [5, 8, 7]
Кодування рядка: 3a2b1c
Декодування рядка: aaabbc
Обертання матриці: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
Пошук за регулярними виразами: ['apple']
Злиття двох відсортованих масивів: [1, 2, 3, 4, 5, 6]
Перевірка на прості числа: True для 29, False для 30
Групування даних за ключем: {'a': [1, 3], 'b': [2]}
Видалення аномальних значень: [10, 12, 23, 23, 16, 23, 21, 16, 22, 21, 14, 17, 22, 20, 19, 15, 25, 18]

Вимоги до середовища: Python 3.x
