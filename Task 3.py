# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов.

import random


array = []
for i in range(10):
    array.append(round(random.uniform(5, 10), 2))

array2 = [round(i % 1, 2) for i in array if i % 1 != 0]

print(f' Array :{array}')
print(f'Fractional array:{array2}')
print(f' {max(array2)} - {min(array2)} = {max(array2) - min(array2)}')
