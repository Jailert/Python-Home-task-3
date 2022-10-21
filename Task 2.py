# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
import random

array = []
for i in range(10):
    array.append(random.randint(1, 10))
print(f'Array : {array}')

size = len(array)//2
changed_array = [array[i] * array[-i - 1] for i in range(size)]

print(f'Changed array : {changed_array}')
