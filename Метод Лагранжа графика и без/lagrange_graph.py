import matplotlib.pyplot as plt

def lagrange(x, y, x_new):
    """
    Вычисляет значение интерполяционного многочлена Лагранжа
    в точках x_new, используя данные x и y.

    Аргументы:
    x - список x-координат опорных точек
    y - список y-координат опорных точек
    x_new - список точек, в которых нужно вычислить интерполяцию

    Возвращает:
    Список значений интерполяционного многочлена Лагранжа в точках x_new
    """
    n = len(x)
    y_new = []

    for x_i in x_new:
        L = 0
        for i in range(n):
            li = 1
            for j in range(n):
                if j != i:
                    li *= (x_i - x[j]) / (x[i] - x[j])
            L += y[i] * li
        y_new.append(L)

    return y_new

# Пример использования
# Исходные данные
x = [0, 1, 2, 3]
y = [1, 4, 9, 16]

# Точки, в которых нужно вычислить интерполяцию
x_new = [x / 100 for x in range(301)]

# Вычисляем интерполяцию
y_new = lagrange(x, y, x_new)

# Построение графика
plt.figure(figsize=(8, 6))
plt.plot(x, y, 'ro', label='Исходные данные')
plt.plot(x_new, y_new, label='Интерполяционный многочлен Лагранжа')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Интерполяция методом Лагранжа')
plt.legend()
plt.grid()
plt.show()