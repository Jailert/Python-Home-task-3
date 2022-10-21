# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.

import random

array = []
sum = 0
for i in range(10):
    array.append(random.randint(1, 10))
    if i % 2 != 0:
        sum = sum + array[i]

print(f'array :{array}')
print(f'sum = {sum}')
