import random
# Размерность матрицы вводится с клавиатуры, заполнить матрицу случайными числами от 10 до 50.
# Найти наибольшую сумму элементов в столбцах матрицы. Вывести индекс столбца с максимальной суммой элементов на экран
M = int(input("Введите рамерность M матрицы: "))
N = int(input("Введите рамерность N матрицы: "))
Matrix = [[random.randint(10, 50) for i in range(M)] for j in range(N)]
for i in range(M):
    print(Matrix[i])
a = 0
b = 0
for i in range(M):
    sum1 = 0
    for j in range(N):
        sum1 += Matrix[j][i]
    if sum1 > a:
        a = sum1
        b = i
print(f'Сумма равна {a}, найдена в столбце {b}')

