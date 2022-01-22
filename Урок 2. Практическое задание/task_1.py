"""
Задание 1.	Написать программу, которая будет складывать, вычитать,
умножать или делить два числа. Числа и знак операции вводятся пользователем.
После выполнения вычисления программа не должна завершаться, а должна
запрашивать новые данные для вычислений. Завершение программы должно
выполняться при вводе символа '0' в качестве знака операции. Если пользователь
вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна
сообщать ему об ошибке и снова запрашивать знак операции.

Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.

Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
- условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ

Решите через рекурсию. Решение через цикл не принимается.

Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):
"""


def counting():
    sign = input('Введите оператор (+, -, *, / или 0 для выхода): ')
    if sign not in ('+', '-', '*', '/', '0'):
        print('Некорректный оператор')
        return counting()
    elif sign == '0':
        return print('Выход.')
    else:
        x = input('Введите первое число: ')
        if x.isdigit():
            x = int(x)
        else:
            print('Вы ввели не число.')
            return counting()
        y = input('Введите второе число: ')
        if y.isdigit():
            y = int(y)
        else:
            print('Вы ввели не число.')
            return counting()
        if sign == '+':
            print(f'Результат: {x + y}')
        elif sign == '-':
            print(f'Результат: {x - y}')
        elif sign == '*':
            print(f'Результат: {x * y}')
        elif sign == '/' and y != 0:
            print(f'Результат: {x / y}')
        else:
            print('На ноль делить нельзя!')
            return counting()
        return counting()


counting()
