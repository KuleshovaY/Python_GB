# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
def div_func(*args):
    try:
      arg_1 = int(input('Введите делимое число: '))
      arg_2 = int(input('Введите делитель: '))
      total = arg_1 / arg_2

    except ValueError:
        return 'Ошибка! Введите число.'
    except ZeroDivisionError:
        return 'Ошибка! На ноль деление запрещено!'

    return total

#print(f'Решение: {div_func()}')
print(div_func())