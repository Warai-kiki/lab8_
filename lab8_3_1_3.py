'''
Завдання 1.3.1 пункт 3
'''
import numpy as np #імпортуємо для роботи з масивами
from random import randint #імпортуємо рандом
x,y = np.array([[randint(-50,50) for i in range(3)] for j in range(3)]),np.array([[randint(-50,50) for k in range(3)] for g in range(3)])
print(f'Матриця 1:\n{x}')#створюємо рандомні матриці
print(f'Матриця 2:\n{y}')
if len(x[0,:])==len(y[:,0]):#перевіяємо рзмірність матриць
    z = np.dot(x,y)#множимо матриці за допомогою фунції dot
    print(f'Добуток матриць 1 і 2:\n{z}')
else:
    print('Розмірності матриць не підходять для множення')