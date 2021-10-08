time = int(input('Введите время в секундах: '))

h = 3600
m = 60

hour = time // 3600
min = (time - (hour * h)) // 60
sec = time - ((hour * h) + (min * m))

print (f'{hour:02d}:{min:02d}:{sec:02d}')