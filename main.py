import math

# Словарь для хранения переменных
variables = {}

# Функции для математических операций
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль!"
    return a / b

def power(a, b):
    return a ** b

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def tan(x):
    return math.tan(x)

def log(x, base=10):
    return math.log(x, base)

def round_num(x, digits=0):
    return round(x, digits)

def factorial(x):
    return math.factorial(x)

# Функция для обработки команд пользователя
def process_command(command):
    if "=" in command:
        parts = command.split("=")
        var_name = parts[0].strip()
        expression = parts[1].strip()
        try:
            variables[var_name] = eval(expression, variables)
        except (SyntaxError, NameError):
            print("Ошибка: неверное выражение!")
    else:
        try:
            return eval(command, variables)
        except (SyntaxError, NameError):
            print("Ошибка: неверное выражение!")

# Интерфейс калькулятора
def calculator():
    print("Для выхода введите 'exit'.")
    while True:
        command = input("Введите команду или выражение: ")
        if command.lower() == 'exit':
            print("Выход из калькулятора.")
            break

        result = process_command(command)
        if result is not None:
            print("Результат: ", result)

if __name__ == "__main__":
    calculator()