'''Дано нечетное натуральное число n. Напишите программу, 
которая печатает равнобедренный звездный треугольник с основанием, равным n.'''

n = int(input())

for i in range(n // 2):
    for j in range(i + 1):
        print('*', end='')
    print()

for i in range(n - n // 2, 0, -1):
    for j in range(i):
        print('*', end='')
    print()