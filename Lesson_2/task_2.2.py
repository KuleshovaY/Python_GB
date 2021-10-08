# Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input()
# Вариант 1
a_list = list (input('Введите элементы списка: '))
for i in range(0, len(a_list)-1, 2):
    a_list[i], a_list[i+1] = a_list[i+1], a_list[i]

print(a_list)
# вариант 2
my_list = input('enter the numbers - ').split()
if len(my_list) % 2 == 0:
    i = 0
    while i < len(my_list):
        el = my_list[i]
        my_list[i] = my_list[i + 1]
        my_list[i +1] = el
        i += 2
else:
    i = 0
    while i < len(my_list) - 1:
        el = my_list[i]
        my_list[i] = my_list[i + 1]
        my_list[i + 1] = el
        i += 2
print(my_list)

# Вариант без цикла

 my_list = list(input('Enter the numbers without space - '))
 idx = len(my_list) if len(my_list) % 2 == 0 else len(my_list) - 1

 my_list[:idx:2], my_list[1:idx:2] = my_list[1:idx:2], my_list [:idx:2]
 print('Измененный список: ', my_list)





