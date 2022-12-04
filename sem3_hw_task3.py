# Задача 3
# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.  
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import os

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
    
title = 'Разница между максимальным и минимальным значением дробной части элементов'
print('-'*len(title))
print(title)
print('-'*len(title))

# получение списка дробных частей из списка вещественных чисел
def get_fraction_parts(float_list: list) -> list:
    fraction_parts = []
    for e in float_list:
        if type(e) != int:
            fraction_parts.append(float('0.' + str(e).split('.')[1]))
    return fraction_parts

# тестовый список
float_nums = [1.1, 1.2, 3.1, 5, 10.01]

# выделяем дробную часть
fractions_lst = get_fraction_parts(float_nums)

# находим разность между max и min дробной части
diff = max(fractions_lst) - min(fractions_lst)

# вывод
print(f'{float_nums} => {diff}')
