def calculate(expression):
    try:
        result = eval(expression)
    except ZeroDivisionError:
        result = "Ошибка: деление на ноль"
    except Exception:
        result = "Ошибка: некорректное выражение"
    return result

# Получение ввода от пользователя
expression = input("Введите математическое выражение: ")

# Вычисление результата и вывод
result = calculate(expression)
print("Результат:", result)
