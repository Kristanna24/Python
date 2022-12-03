lesson_05.py
# -------------------------------- 1 ---------------------------------------
with open('new_file.txt', 'a', encoding='utf-8') as n_f:
    while True:
        user_str = input('Введите построчно данные, для завершения нажмите Enter: ')
        n_f.write(f'{user_str}\n')
        if not user_str:
            break

# -------------------------------- 2 ---------------------------------------
with open('new_file.txt', 'r', encoding='utf-8') as n_f:
    my_line = n_f.readlines()
    for str, word in enumerate(my_line, 1):
        num_words = len(word.split())
        print(f'Строка {str} содержит {num_words} слова')
    print(f'Всего строк: {str} шт.')

# -------------------------------- 3 ---------------------------------------
with open('new_file.txt', 'r', encoding='utf-8') as n_f:
    dict = {liner.split()[0]: float(liner.split()[1]) for liner in n_f}
    print(f'Средняя зарплата: {round(sum(dict.values()) / len(dict), 3)}')
    print(f'Фамилии, чья заработная плата менее 20 тыс.руб. {[i[0] for i in dict.items() if i[1] < 20000]}')

# -------------------------------- 4 ---------------------------------------
rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('new_file_1.txt', 'w', encoding='utf-8') as n_f_1:
   with open('new_file.txt', 'r', encoding='utf-8') as n_f:
      n_f_1.writelines([string.replace(string.split()[0], rus.get(string.split()[0])) for string in n_f])

# -------------------------------- 5 ---------------------------------------
from random import randint

with open('new_file.txt', 'w', encoding='utf-8') as n_f:
   my_list = [randint(1, 10) for i in range(10)]
   n_f.write(''.join(map(str, my_list)))
print(f'Общая сумма элементов: {sum(my_list)}')

# -------------------------------- 6 ---------------------------------------
with open('new_file.txt', 'r', encoding='utf-8') as n_f:
   for string in n_f:
      str_1 = ''.join((i if i in '0123456789' else ' ') for i in string)
      str_2 = [int(i) for i in str_1.split()]
      print(f'{string.split()[0]} {sum(str_2)}')

# -------------------------------- 7 ---------------------------------------
import json
with open('new_file_1.json', 'w', encoding='utf-8') as n_f_1, open('new_file.txt', 'r', encoding='utf-8') as n_f:

   profit = {spring.split()[0]: int(spring.split()[2]) - int(spring.split()[3]) for spring in n_f}
   f_up = [i for i in profit.values() if i > 0]
   result = [profit, {'средняя прибыль': round(sum(f_up) / len(f_up))}]

   json.dump(result, n_f_1, ensure_ascii=False, indent=4)

