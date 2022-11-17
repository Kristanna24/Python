lesson_01.py
# -----1
name = input('Введите свое имя: ')
age = int(input('Сколько Вам лет: '))
time = float(age + 1.5)
print(f'Привет,', {name}, 'в', {time}, 'вы окончите курс Python...')

# -----2
seconds = int(input('Введите время в секундах: '))
seconds %= 86400
hour = seconds // 3600
seconds %= 3600
minute = seconds // 60
seconds %= 60
print('%d:%d:%d' % (hour, minute, seconds))

# -----3
n = (input('Введите число: '))
a = n
b = n + n
c = n + n + n
result = ('%s + %s + %s' % (a, b, c))
print(result, '=', int(a[:]) + int(b[:]) + int(c[:]))

# -----4
count = int(input('Введите целое, положительное число: '))
number = 0
while count > 0:
    number = max(number, count % 10)
    count //= 10
print(number)

# -----5
a = int(input('Введите сумму выручки фирмы: '))
b = int(input('Введите сумму издержек фирмы: '))
if a == b:
    print('Вы достигли точки безубыточности')
elif a > b:
    print('Ваша фирма в прибыли на: ', a - b, 'руб.')
else:
    print('Ваша фирма в убытке на: ', b - a, 'руб.')

# -----6
a = int(input('Введите сумму выручки фирмы: '))
b = int(input('Введите сумму издержек фирмы: '))
if a > b or b == 0:
    print('Ваша фирма в прибыли на: ', a - b, 'руб.')
    profit = a - b
    rent = int((profit / a) * 100)
    print('Рентабельность составила: ', rent, 'руб.')
    human = int(input('Введите численность сотрудников фирмы: '))
    c = float(profit / (human * 1000))
    print('Прибыль на одного сотрудника составляет: ', c, 'руб.')
elif a < b:
    print('Ваша фирма в убытке на: ', b - a, 'руб.')
else:
    print('Вы достигли точки безубыточности')

# -----7
a = int(input('Введите сумму выручки фирмы: '))
b = int(input('Введите сумму издержек фирмы: '))
if a > b or b == 0:
    print('Ваша фирма в прибыли на: ', a - b, 'руб.')
    profit = a - b
    rent = int((profit / a) * 100)
    print('Рентабельность составила: ', rent, 'руб.')
    human = int(input('Введите численность сотрудников фирмы: '))
    c = float(profit / (human * 1000))
    print('Прибыль на одного сотрудника составляет: ', c, 'руб.')
elif a < b:
    print('Ваша фирма в убытке на: ', b - a, 'руб.')
else:
    print('Вы достигли точки безубыточности')


