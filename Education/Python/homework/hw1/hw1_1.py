# Решение кубического уравнения
import math
import numpy

a0 = int(input('Введите значение a: '))
a1 = int(input('Введите значение b: '))
a2 = int(input('Введите значение c: '))
a3 = int(input('Введите значение d: '))

a = a1/a0
b = a2/a0
c = a3/a0

q = (a**2 - 3 * b)/9
r = (2 * a**3 - 9 * a * b + 27 * c)/54
s = q**3 - r**2

if s > 0:
    fi = (1/3) * math.acos(r / math.sqrt(q**3))
    x1 = -2 * math.sqrt(q) * math.cos(fi) - a/3
    x2 = -2 * math.sqrt(q) * math.cos(fi+2 * math.pi/3) - a/3
    x3 = -2 * math.sqrt(q) * math.cos(fi-2 * math.pi/3) - a/3
    print(f'x1 = {(numpy.round(x1, 2))}, x2 = {(numpy.round(x2, 2))}, x3 = {(numpy.round(x3, 2))}')
elif s < 0:
    if q > 0:
        fi = (1/3) * math.acosh(math.fabs(r)/math.sqrt(q**3))
        x1 = -2 * numpy.sign(r)*math.sqrt(q)*math.cosh(fi) - a/3
        x2 = numpy.sign(r) * math.sqrt(r) * math.cosh(fi) - a/3 + 1j * (math.sqrt(3) * math.sqrt(q)*math.sinh(fi))
        x3 = numpy.sign(r) * math.sqrt(r) * math.cosh(fi) - a/3 - 1j * (math.sqrt(3) * math.sqrt(q)*math.sinh(fi))
        print(f'x1 = {(numpy.round(x1, 2))}, x2 = {(numpy.round(x2, 2))}, x3 = {(numpy.round(x3, 2))}')
    elif q < 0:
        fi = (1/3) * math.asinh(math.fabs(r) / math.sqrt(math.fabs(q)**3))
        x1 = -2 * numpy.sign(r) * math.sqrt(math.fabs(q)) * math.sinh(fi) - a/3
        x2 = numpy.sign(r) * math.sqrt(math.fabs(q)) * math.sinh(fi) - a/3 + 1j * (math.sqrt(3) * math.sqrt(math.fabs(q)) * math.cosh(fi))
        x3 = numpy.sign(r) * math.sqrt(math.fabs(q)) * math.sinh(fi) - a/3 - 1j * (math.sqrt(3) * math.sqrt(math.fabs(q)) * math.cosh(fi))
        print(f'x1 = {(numpy.round(x1, 2))}, x2 = {(numpy.round(x2, 2))}, x3 = {(numpy.round(x3, 2))}')
    else:
        x1 = -(c - (a**3)/27)**(1/3) - a/3
        x2 = (-a+x1)/2 + 1j * ((1/2) * math.sqrt(math.fabs((a-3 * x1) * (a+x1)-4*b)))
        x3 = (-a+x1)/2 - 1j * ((1/2) * math.sqrt(math.fabs((a-3 * x1) * (a+x1)-4*b)))
        print(f'x1 = {(numpy.round(x1, 2))}, x2 = {(numpy.round(x2, 2))}, x3 = {(numpy.round(x3, 2))}')
else:
    x1 = -2 * r**(1/3) - a/3
    x2 = r**(1/3) - a/3
    print(f'x1 = {(numpy.round(x1, 2))}, x2 = {(numpy.round(x2, 2))}')
