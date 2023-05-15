from sympy import symbols, diff, solve
from sympy import Symbol

def is_real(expr):
    return expr.is_real

# Variablarni aniqlash
x, y = symbols('x y')

# Funksiyani aniqlash
z = x**2 + x*y + y**2 + 9*x*x - 6*y + 20

# Gradientni topish
z_x = diff(z, x)
z_y = diff(z, y)

# Tenglamaga tenglashtirish
eq1 = z_x
eq2 = z_y
eq3 = y + 20*x

# Noto'g'ri koordinatalar
solutions = solve((eq1, eq2, eq3), (x, y))
for sol in solutions:
    if sol[0].is_real and sol[1].is_real:
        print(f"({sol[0]}, {sol[1]})")

# Minimum qiymat
z_min = z.subs({x: -1/13, y: 20/13})
print(f"Minimum qiymat: {z_min}")