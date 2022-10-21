# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.

k = int(input('Enter k = '))
fib = [0, 1]
for i in range(2, k + 1):
    fib.append(fib[i-2] + fib[i-1])
fib.pop(2)

negfib = [1, 0]
for i in range(2, k + 2):
    negfib.append(negfib[i-2] - negfib[i-1])
negfib.reverse()

fullfib = negfib + fib
print(fullfib)
