# Задача 2
# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.  
# Пример:  
# [2, 3, 4, 5, 6] =>[12,15,16]    ([2*6, 3*5, 4*4]);
# [2, 3, 5, 6] => [12,15]         ( [2*6, 3*5]) 
# В скобках пример, как это работает!!!

from random import randint
import os

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
    
title1 = 'Произведение пар чисел списка.'
title2 = '(парой считаем первый и последний элемент, второй и предпоследний и т.д.)'
print('-'*len(title2))
print(title1)
print(title2)
print('-'*len(title2))

# тестовый список
# nums = [2, 3, 4, 5, 6]
# nums = [2, 3, 5, 6]

def create_random_int_list(n: int) -> list:
    min_n, max_n = 1, 10
    int_list = [randint(min_n, max_n) for i in range(n)]
    return int_list

num = int(input('Введите сколько будет чисел в списке: '))
nums = create_random_int_list(num)

mults = []
middle = len(nums) // 2

if len(nums) % 2 == 0:
    for i in range(middle):
        mults.append(nums[i]*nums[-i-1])
else:
    for i in range(middle + 1):
        mults.append(nums[i]*nums[-i-1])

print(f'{nums} -> {mults}')
