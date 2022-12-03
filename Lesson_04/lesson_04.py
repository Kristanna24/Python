lesson.py
lesson_04.py
# ---------------------------------1---------------------------------
import sys


def premiya(a, b, c):
    return (a * b) + c


command = sys.argv[1]
if command == 'premiya':
    print(f'Размер заработной платы составил: {premiya(15, 250, 2000)}')

# ---------------------------------2---------------------------------
my_list = []
list = [int(i) for i in input('Введите список чисел, через пробел: ').split()]
for i in range(1, len(list)):
    if list[i] > list[i-1]:
        (my_list.append(list[i]))

print(f'Исходный список:  {list}')
print(f'Список, элементы которого больше предыдущего: {my_list}')

# ---------------------------------3---------------------------------
my_list = [n for n in range(20, 240) if n % 20 == 0 or n % 21 == 0]
print('Список чисел кратных 20 или 21 в диапазоне от 20 до 240: ', my_list)

# ---------------------------------4---------------------------------
my_list_1 = [2, 9, 11, 24, 2, 11]
print('Введите элементы списка: ', my_list_1)
my_list_2 = [i for i in my_list_1 if my_list_1.count(i) == 1]
print('Элементы списка, не имеющие повторений: ', my_list_2)

# ---------------------------------5---------------------------------
from functools import reduce
def my_func(x, y):
    return x * y

print(reduce(my_func, range(100, 1001, 2)))

# ---------------------------------6---------------------------------
from itertools import cycle
print('Итератор, повторяющий элементы некоторого списка, определенного заранее')
list_1 = [5, 7, 9, 2, 4, 6, 8, 1, 3]
for x, y in enumerate(cycle(list_1)):
    print(y, end=' ')
    if x > 50:
        print()
        break

# ---------------------------------7---------------------------------
from math import factorial

def fact(n):
    for i in range(n):
        print(i+1, end='! = ')
        yield factorial(i+1)

x = int(input('Введите число, для вычисления факториала: '))
for el in fact(x):
    print(el)