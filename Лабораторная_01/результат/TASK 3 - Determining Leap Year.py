# Задание 1.3 - Определение високосного года
def read_int(prompt):
    # безопасный ввод целого числа с повторным запросом при ошибке
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка: введите целое число!")

year = read_int("Введите год: ")

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"Год {year} является високосным")
else:
    print(f"Год {year} не является високосным")