field = input("Напишите любимые фрукты: ")
name = []
num = 1
for el in range(field.count(' ') + 1):
    name = field.split()
    if len(str(name)) <= 10:
        print(f" {num} {name [el]}")
        num += 1
    else:
        print(f" {num} {name [el] [0:10]}")

# вариант решения
s = input('Enter thr numbers with space ').split()
for i, word in enumerate(s, 1):
    print(i, word) if len(word) <= 10 else print(i, word[:10])

# вариант решения
my_string = input('Введите строку из несколькихслво через пробел: ').split()

for i, word in enumerate(my_string, 1):
    print(f'{i} {word[:10]}')

