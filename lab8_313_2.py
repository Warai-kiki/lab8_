'''
Завдання 1.3.1 пункт 3
'''
import numpy as np #імпортуємо для роботи з масивами
from random import randint #імпортуємо рандом
x,y,h= np.array([[randint(-50,50) for i in range(3)] for j in range(3)]),np.array([[randint(-50,50) for k in range(3)] for g in range(3)]),np.zeros((3,3), dtype=int)
print(f'Матриця 1:\n{x}')#створюємо рандомні матриці
print(f'Матриця 2:\n{y}')
if len(x[0,:])==len(y[:,0]):#перевіяємо рзмірність матриць
    z = x*y #множимо за допомогою оператора
    v = np.multiply(x,y)#або відповідної функції, але це поелементне множення матриць
    print(f'Добуток матриць 1 і 2 по-елементно:\n{z}\n{v}')
    for i in range(len(x[0,:])):#проходимось по рядкам 1 матриці
        for j in range(len(y[:,0])):#потім по стовпчикам і рядкам другої
            for k in range(len(y[0,:])):
                h[i][j] += x[i][k] * y[k][j]#і за допомогою циклу заповнюємо нульову матрицю
    print(f'Добуток матриць 1 і 2:\n{h}')
else:
    print('Розмірності матриць не підходять для множення')