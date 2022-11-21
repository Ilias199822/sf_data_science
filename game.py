"""Игра: угадай число"""
import numpy as np

number = np.random.randint(1,101) # загадываем число

# количество попыток
count = 0

while True:
    count += 1
    predict_number = int(input('Введите число: '))
    if predict_number > number:
        print('Введите число меньше !')
    elif predict_number < number:
        print('Введите число больше!')
    else:
        print(f'Поздравляю вы угадали число {number} ! за {count} попыток')
        break # конец игры, выход из цикла
