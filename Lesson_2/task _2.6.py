i = 1
goods = []
n = int(input('Сколько товаров хотите ввести? '))
for _ in range(n):
    name = input('Введите название товара ')
    price = int(input('Введите цену '))
    quantity = int(input('Введите колличество '))
    measure = input('введите единицы измерения ')
    goods.append((i, {'название': name, 'цена': price, 'количество': quantity, 'ед': measure}))
    i += 1
print(goods)
goods_dict = {'название': [], 'цена': [], 'количество': [], 'ед': []}
for good in goods:
    goods_dict['название'].append(good[1]['название'])
    goods_dict['цена'].append(good[1]['цена'])
    goods_dict['количество'].append(good[1]['количество'])
    if good[1]['ед'] not in goods_dict['ед']:
        goods_dict['ед'].append(good[1]['ед'])
print(goods_dict)
