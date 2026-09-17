# Задание 1.1 - Калькулятор площади треугольника
import math

def read_float(prompt):
    # безопасный ввод числа с повторным запросом при ошибке
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введите число!")

print("Введите стороны треугольника:")
a = read_float("Сторона a: ")
b = read_float("Сторона b: ")
c = read_float("Сторона c: ")

if a + b > c and a + c > b and b + c > a:
    p = (a + b + c) / 2                # полупериметр
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(f"Площадь треугольника: {s:.2f}")
else:
    print("Треугольник с такими сторонами не существует")