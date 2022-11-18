lesson_02.py
# -----------1
list_kri = [24, 'Kris', 5j, None, -5, False, 5.5]


def type_one(element):
    for element in range(len(list_kri)):
        print(type(list_kri[element]))
    return


type_one(list_kri)

# -----------2
list = list(input("Введите элементы списка: "))

list[:-1:2], list[1::2] = list[1::2], list[:-1:2]

print(list)

# -----------3
month = int(input('Введите номер месяца: '))
seasons_dict = {1: 'зима', 2: 'весна', 3: 'лето', 4: 'осень'}

if 0 < month <= 2 or month == 12:
    print(seasons_dict.get(1))

elif 2 < month <= 5:
    print(seasons_dict.get(2))

elif 5 < month <= 8:
    print(seasons_dict.get(3))


elif 8 < month <= 11:
    print(seasons_dict.get(4))

else:
    print('Вы ввели неверный номер')

# -----------4
my_text = str(input('Введите предложение: '))
word = []
num = 1
for i in range(my_text.count(' ') + 1):
    word = my_text.split()
    if len(str(word)) <= 10:
        print(f' {num} {word[i]}')
        num += 1
    else:
        print(f' {num} {word[i][0:10]}')
        num += 1

# -----------5
my_list = [24, 11, 9, 2]
print(my_list)
element = int(input('Введите новый элемент в рейтинг: '))
my_list.append(element)
my_list.sort(reverse=True)
print(my_list)

