def Zeidel(A, B, x0, epsilon, maxIteration=50):
    sizeMatrix = len(B)
    x = x0
    countIterations = 1
    flagEpsilon = False
    while countIterations <= maxIteration and not flagEpsilon:
        x_old = x.copy()  # Сохраняем старые значения переменных
        for i in range(sizeMatrix):
            sum1 = sum(A[i][j] * x[j] for j in range(i))
            sum2 = sum(A[i][j] * x[j] for j in range(i + 1, sizeMatrix))
            x[i] = (B[i] - sum1 - sum2) / A[i][i]

        print(countIterations, end="      | ")
        for i in x:
            print(f" {i:.5f}", end=" |")

        error = max(abs(x[i] - x_old[i]) for i in range(sizeMatrix))  # Проверяем изменение значений переменных
        if error < epsilon:
            flagEpsilon = True

        countIterations += 1
        print()

# Тестовые данные
A = [[10, 2, -1], [-2, -6, -1], [1, -3, 12]]
B = [5, 24, 36]
x0 = [0, 0, 0]
epsilon = 0.01

# Вызов функции для решения системы методом Зейделя
print()
print("Number |  x1      |  x2      |  x3     |")
Zeidel(A, B, x0, epsilon)
