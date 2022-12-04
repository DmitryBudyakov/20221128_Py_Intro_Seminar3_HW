# Задача 4
# Напишите программу, которая будет преобразовывать
# десятичное число в двоичное.  
# Пример:
# 45 -> 101101  
# 3 -> 11  
# 2 -> 10

import os

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

# функция возвращает строку с двоичным числом
def dec_to_bin(num: int) -> str:
    if num == 0:
        return 0
    bin_num = ''
    while (num != 0):
        bin_num += str(num % 2)
        num //= 2
    bin_num = ''.join(reversed(bin_num))    # разворот строки
        
    return bin_num

title = 'Преобразование десятичного числа в двоичное'
print('-'*len(title))
print(title)
print('-'*len(title))


dec_num = int(input('Введите натуральное число: '))
dec_num_orig = dec_num

bin_num = dec_to_bin(dec_num)
    
print(f'dec: {dec_num_orig} -> bin: {bin_num}')
