'''
Завдяння 1.3.1
'''
import timeit #імпортуємо для того щоб дізнатись час роботи програми
import numpy as np #імпортуємо для роботи з масивами
from random import randint #для рандомного вибору чисел
while True: #зациклюємо всю програму
    while True:#завдання 1
        try: #перевірка при входженні
            n = int(input('1) Введіть розмір масиву: '))#вводиться довжина масиву
            print('Введіть елементи масиву: ')
            a = np.array([int(input('')) for _ in range(n)])#вводяться елнменти в масив за допомогою генератора списків
            break
        except ValueError or KeyError or NameError or TypeError:
            print('Введіть ще раз')
    z = a[::-1]#за допомогою зрізу розвертаємо матрицю
    print(f'Обернений масив: {z}\n')
    #завдання 2
    x = np.zeros((3,3), dtype=int)# створюємо масив з нулів
    print('2) Введіть елементи матриці')
    while True:
        try:
            for i in range(3):#при введенні замінюємо кожен елемент матриці; перебирає рядки
                for j in range(3):#перебирає стовпчики
                    x[i][j] = int(input(''))
            break
        except ValueError or KeyError or NameError or TypeError:
            print('Введіть ще раз')
    y = np.zeros((3,3), dtype=int)#ще один список з нулів
    for i in range(3):#знову перебираємо кожен елемент
        for j in range(3):
            y[i][j] = x[j][i]#і змінюємо місцями рядки і стовпчики прицьому заповняючи другу матрицю
    print(f'Ваша матриця: \n{x}')
    print(f'Транспоована атриця:\n{y}\n')
    #завдання 3
    f,s,h = np.array([[randint(-50,50) for i in range(3)] for j in range(3)]),np.array([[randint(-50,50) for i in range(3)] for j in range(3)]),np.zeros((3,3), dtype=int)
    print(f'3) Матриця 1:\n{f}')#створюемо дві матриці з рандомними елементами і одну з нулями
    print(f'Матриця 2:\n{s}')
    for i in range(3):#перебираєм кожен елемент нульової матриці щоб замінити на добуток двох перших
        for j in range(3):
            h[i, 0] = f[i, 0] * s[0, 0] + f[i, 1] * s[1, 0] + f[i, 2] * s[2, 0]#множення матриць
            h[i, 1] = f[i, 1] * s[0, 0] + f[i, 1] * s[1, 1] + f[i, 2] * s[2, 1]
            h[i, 2] = f[i, 2] * s[0, 0] + f[i, 1] * s[1, 2] + f[i, 2] * s[2, 2]
    print(f'Добуток матриць 1 і 2:\n{h}\n')
    #завданн 4
    k = np.array([[randint(-50,50) for i in range(4)] for j in range(4)])#створюем рандомну матрицю за допомогою генератора списків
    print(f'4) Початкова матриця: \n {k}')
    for i in range(4):#перебираємо кожен її елемент
        for j in range(4):
            if k[i][j]<0:#визначаємо елементи що менше нуля
                k[i][j] = 0#замінюємо їх на нуль
    print(f'Кінцева матриця:\n {k}\n')

    print('Запустити програму ще раз? Напишіть так чи ні')
    l = input('')#цикл умові якщо хоче ористувач ще раз запустити програму
    if l == 'так':
        continue#програма починається заново
    else:
        break#цикл обривається

t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print('Час роботи програми: {:.3f}'.format(t))#показує час виконання програми

