def secant(f, a, b, tol=10**-7):
    if f(a) * f(b) >= 0:
        raise ValueError("Значения функции на концах интервала должны иметь противоположные знаки")

    while abs(b - a) > tol:
        x = b - f(b) * (b - a) / (f(b) - f(a))
        if f(x) == 0:
            return x
        elif f(a) * f(x) < 0:
            b = x
        else:
            a = x

    return (a + b) / 2

def function(x):
    return x**3 - 2*x + 1 #x^3 - 2*x + 1 = 0


interval = [-2, 2]
print(f"f({interval[0]}) = {function(interval[0])}")
print(f"f({interval[1]}) = {function(interval[1])}")

root = secant(function, interval[0], interval[1])

print(f"Корень f(x) = 0 на интервале [{interval[0]}, {interval[1]}]: {root:.6f}")