import math

# Определение функций для уравнений
def urav1(x, y):
    return (x * y) - 2.3

def urav2(x, y):
    return (x / y) - 1.9

# Функция для решения системы линейных уравнений методом Гаусса
def gauss(matrix):
    n = len(matrix)
    m = len(matrix[0])

    # Прямой ход (приведение к верхнетреугольному виду)
    for j in range(m - 2):
        pivot = matrix[j][j]
        for i in range(j + 1, n):
            factor = matrix[i][j] / pivot
            for k in range(j, m):
                matrix[i][k] -= factor * matrix[j][k]

    # Обратный ход (решение системы)
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = matrix[i][m - 1]
        for j in range(i + 1, n):
            x[i] -= matrix[i][j] * x[j]
        x[i] /= matrix[i][i]

    return x

n = 2  # Количество уравнений
m = 3  # Количество элементов в строке (коэффициенты + свободные члены)
shag_count = 3  # Количество шагов
shag = 0  # Счетчик шагов

# Начальные значения матрицы
mass = [[1, 2, -0.3], [1, -2, 0.1]]
x_shag = [2, 1]  # Начальные приближения x и y

for shag in range(shag_count):
    print(f"\n==========Step {shag + 1}==========")
    for row in mass:
        print(*row, sep="\t|\t")  # Вывод матрицы

    # Решение системы методом Гаусса
    arr = gauss(mass)
    print("\nGauss:")
    print(*arr, sep="    ")
    print("=========")

    # Вычисление новых приближений x и y
    for i in range(n):
        x_shag[i] -= arr[i]

    x, y = x_shag
    print(f"X{shag + 1}:  x     y")
    print(f"{x:.15f}\t{y:.15f}")
    print("=========")

    # Обновление матрицы для следующего шага
    mass[0][0] = y
    mass[0][1] = x
    mass[1][0] = 1 / y
    mass[1][1] = -(x / (y ** 2))
    mass[0][2] = urav1(x, y)
    mass[1][2] = urav2(x, y)

    input("Нажмите Enter для продолжения...")