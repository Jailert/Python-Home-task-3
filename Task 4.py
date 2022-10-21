# Напишите программу, которая будет
# преобразовывать десятичное число в двоичное.

number = int(input())
double = ""
while number != 0:
    double = str(number % 2) + double
    number = number // 2
print(double)
