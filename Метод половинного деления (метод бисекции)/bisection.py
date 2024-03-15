def bisection(f, a, b, tol=10**-7):
    if f(a) * f(b) >= 0:
        raise ValueError("Значения функции на концах интервала должны иметь противоположные знаки")

    while abs(b - a) > tol:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2

def function(x):
    return x**3 - 2*x + 1 #x^3 - 2*x + 1 = 0


interval = [-2, 2]
print(f"f({interval[0]}) = {function(interval[0])}")
print(f"f({interval[1]}) = {function(interval[1])}")

root = bisection(function, interval[0], interval[1])

print(f"Корень f(x) = 0 на интервале [{interval[0]}, {interval[1]}]: {root:.6f}")

