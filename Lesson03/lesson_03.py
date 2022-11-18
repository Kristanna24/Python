lesson_03.py
# -----------------------------------1-----------------------------------
def x():
    a = float(input(f'Введите знаменатель: '))
    b = float(input(f'Введите делитель: '))

    return a / b if b else 0

result = x()
print(f'Итог: {result:.2f}')

# -----------------------------------2-----------------------------------
def result():
    name = input('Введите свое имя: ')
    surname = input('Введите свою фамилию: ')
    date = input('Введите год рождения: ')
    city = input('Введите город проживания: ')
    email = input('Введите электронную почту: ')
    tel = input('Введите свой номер телефона: ')
    return name, surname, date, city, email, tel

a, b, c, d, i, f = result()
print(f'Ваше имя: {a}, фамилия: {b}, год рождения: {c}, вы проживаете в {d}, адрес электронной почты {i}, номер телефона {f})

# -----------------------------------3-----------------------------------
def my_func(a, b, c):
    if (a + b) > (a + c) and (a + b) > (b + c):
        return a + b
    if (a + c) > (a + b) and (a + c) > (b + c):
        return a + c
    if (b + c) > (a + b) and (b + c) > (a + c):
        return b + c


try:
    n1 = int(input("a = "))
    n2 = int(input("b = "))
    n3 = int(input("c = "))
    print(f"Сумма двух максимальных чисел: {my_func(n1, n2, n3)}")
except ValueError as e:
    print(f"{e}")

 # -----------------------------------4-----------------------------------
 def my_func(x, y):
    i = x
    for _ in range(abs(y) - 1):
        x *= i
    return 1 / x


print(my_func(4, 2))

# -----------------------------------5-----------------------------------
def my_func():
    total = 0
    a = False
    while not a:
        user_num = input('Введите числа или нажмите q для выхода: ').split()
        result = 0
        for i in range(len(user_num)):
            if user_num[i] == 'q':
                a = True
                break
            else:
                result += int(user_num[i])
        total += result
        print(total)

# -----------------------------------6-----------------------------------
def int_func():
    word = input('Введите слова через пробел: ')
    return word.title()


print(int_func())
