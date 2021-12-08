shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

detail = input('Введите название детали: ')
quantity_detail = 0
total_cost = 0

for i in shop:
        quantity_detail += i.count(detail)
        if i.count(detail) > 0:
                total_cost += i[1]

print('Количество деталей: ', quantity_detail)
print('Общая стоимость: ', total_cost)

