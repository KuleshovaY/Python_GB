my_list = [7, 5, 3, 3, 2]
number = int(input("Введите натуральное число: "))
num = my_list.count(number)

for element in my_list:
    if num > 0:
        a = my_list.index(number)
        my_list.insert(a + num, number)
        break
    else:
        if number > element:
            b = my_list.index(element)
            my_list.insert(b, number)
            break
        elif number < my_list[len(my_list) - 1]:
            my_list.append(number)
print(my_list)

# вариант решения

rating = [7, 5, 3, 3, 2]
for _ in range(3):
    i = int(input())
    flag = False
    for j in range (len(rating)):
        if rating[j] < i:
            rating.insert(j, i)
            flag = True
            break
    if not flag:
        rating.append(i)
    print(*rating)



