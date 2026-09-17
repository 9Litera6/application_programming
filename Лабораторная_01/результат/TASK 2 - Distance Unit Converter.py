# Задание 1.2 - Конвертер единиц измерения расстояния
def read_int(prompt):
    # ввод целого числа от 1 до 6 с проверкой
    while True:
        try:
            v = int(input(prompt))
        except ValueError:
            print("Ошибка: введите целое число!")
            continue
        if 1 <= v <= 6:
            return v
        print("Ошибка: введите число от 1 до 6")

def read_float(prompt):
    # ввод неотрицательного числа с проверкой
    while True:
        try:
            v = float(input(prompt))
        except ValueError:
            print("Ошибка: введите число!")
            continue
        if v >= 0:
            return v
        print("Ошибка: расстояние не может быть отрицательным")

# переводные коэффициенты к метрам: км, м, см, мм, миля, ярд
factors = [1000, 1, 0.01, 0.001, 1609.34, 0.9144]
names = ["км", "м", "см", "мм", "mi", "yd"]

print("1 - километры (км), 2 - метры (м), 3 - сантиметры (см)")
print("4 - миллиметры (мм), 5 - мили (mi), 6 - ярды (yd)")

from_unit = read_int("Исходная единица: ") - 1
to_unit = read_int("Целевая единица: ") - 1
value = read_float("Введите значение для конвертации: ")

# сначала переводим в метры, потом из метров в целевую единицу
meters = value * factors[from_unit]
result = meters / factors[to_unit]

print(f"Результат: {value} {names[from_unit]} = {result:.2f} {names[to_unit]}")