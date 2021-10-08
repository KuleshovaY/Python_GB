revenue = int(input('Введите сумму выручки за 1 квартал: '))
costs = int(input('Введите сумму издержек за 1 квартал: '))
profit_margin = revenue / costs

if revenue > costs:
    print(f'Прибыльный бизнес. Рентабельность выручки {profit_margin} рублей')
    workers = int(input('Введите колличество сотрудников: '))
    profit = revenue / workers
    print(f'Прибыль в расчете на одного сотрудника {profit} рублей')
elif revenue == costs:
    print('Бизнес работет в ноль')

else:
    print('Убыточный бизнес')
