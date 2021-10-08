# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

# Первый вариант
def my_func(x, y):
    return x ** y
print (my_func(2, -4))

# Второй вариант
def my_func(x, y):
    res = 1
    for i in range(abs(y)):
        res *= x
    if y >= 0:
        return res
    else:
        return 1 / res

print(my_func(2, -2))


# вариант решения
def my_func(x, y):
    try:
        x = float(x)
        y = int(y)
    except ValueError:
        print('Программа работает только с действительными x и отрицательными y')
              return
    if x <= 0 or y >= 0:
        print ('программа работает только с положительными x и отрицательными y')
        return
    return x ** y
print(round(my_func(2, -2), 10))


# вариант решения
def pow_negative(x, y):
    try:
        x = float(x)
        y = int(y)
    except ValueError:
        print('Программа работает только с действительными x и отрицательными y')
              return
    if x <= 0 or y >= 0:
        print ('программа работает только с положительными x и отрицательными y')
        return
    result =1
    for _ in range(abs(y)):
        result /= x
    return result
print(round(pow_negative(input('Введите действительный положительный x:'),
                         input('Введите целый отрицательный y'))

