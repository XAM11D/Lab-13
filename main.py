
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


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def process_batches(numbers, batch_size):
    max_values = []
    for i in range(0, len(numbers), batch_size):
        batch = numbers[i:i+batch_size]
        max_values.append(max(batch))
    return max_values

import re


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


def rotate_matrix(matrix):
    n = len(matrix)
    rotated = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated[j][n - i - 1] = matrix[i][j]
    return rotated


def regex_search(strings, pattern):
    return [string for string in strings if re.search(pattern, string)]


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

import math


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def group_by_key(data, key):
    grouped = {}
    for item in data:
        grouped.setdefault(item[key], []).append(item['value'])
    return grouped


def remove_outliers(numbers):
    mean = sum(numbers) / len(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    std_deviation = math.sqrt(variance)
    return [x for x in numbers if abs(x - mean) <= 2 * std_deviation]




