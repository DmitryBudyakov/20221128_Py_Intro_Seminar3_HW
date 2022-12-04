# Задача 5
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.(Дополнительно)
# Пример:
# для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

import os

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

# расчет значения числа фибоначчи
def fib_pos(num: int) -> int:
    if num == 0:
        return 0
    elif num == 1 or num == 2:
        return 1
    else:
        return fib_pos(num - 2) + fib_pos(num - 1)
    
# расчет значения числа негафибоначчи (через фибоначчи)
def fib_neg(num: int) -> int:
    return (-1)**(num+1) * fib_pos(num)

title = 'Список чисел Фибоначчи вклчая отрицательные индексы'
print('-'*len(title))
print(title)
print('-'*len(title))

n = int(input('Введите натуральное число: '))

# список чисел фибоначчи
fib_pos_list = [fib_pos(i) for i in range(n + 1)]

# список чисел негафибоначчи
fib_neg_list = [fib_neg(i) for i in range(1, n + 1)]
fib_neg_list.reverse()

# оба списка вместе
fib_both = fib_neg_list + fib_pos_list

# вывод
print(f'n = {n} -> {fib_both}')
