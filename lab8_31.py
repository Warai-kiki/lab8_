'''
Завдання 1.3.2 завдання 1
'''
import random#імпортуємо рандом
import timeit#імпортуємо для того щоб дізнатись час роботи програми
t = 'Для кожного алгоритму необхідно підготувати тести, що підтверджують працездатність програми'# текст, в котором проводится поиск
print(t)
while True:#зациклили програму
    while True:
        try:#перевірка
            x = input('Хочете самостійно ввести підрядок? Напишіть так чи ні ') #користувач вибирає рандом чи ведення власноруч
            if x == 'ні':
                s = ['необхідно','що','кожного']#шукані підрядки
                y = random.choice(s)#рандомно обирається слово
                print(f'Підрядок: {y}')
            else:
                y = input('Введіть свій підрядок: ')#користувач вводить підрядок
            break
        except ValueError or NameError or TypeError:
            print('Введіть ще раз')
    i = -1#вводимо додаткові зміні для нашого алгоритму; лічильник
    j = 0
    while (j < len(y)) and i < (len(t) - len(y)): #починається алгоритм лінійного пошуку
        j = 0  #на кожному кроці зсуваємся лише на одну позицію
        i += 1
        while j < len(y) and y[j] == t[i + j]:
            j += 1
    if j == len(y): #якщо немає куди зсівати, отже ми знайшли наш елемент
        print(f'Підрядок  на позиції {i + 1} ')
    else:
        print('Підрядок не знайдено')

    print('Запустити програму ще раз? Напишіть так чи ні')
    l = input('')  # цикл умови якщо хоче користувач ще раз запустити програму
    if l == 'так':
        continue  # програма починається заново
    else:
        break  # цикл обрівається
t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print('Час роботи програми: {:.3f}'.format(t))