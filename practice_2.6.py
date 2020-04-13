data = []

while True:
    count = input('Введите количество загружаемых товаров:\n')
    if count.isdigit():
        count = int(count)
        break
    else:
        print('Ошибка, необходимо ввести число:')

i = 1
while True:
    name = input(f'Введите название {i}-го товара:\n')
    while True:
        cost = input(f'Введите значение цены {i}-го товара:\n')
        if cost.isdigit():
            cost = int(cost)
            break
        else:
            print('Ошибка, необходимо ввести число:')
    while True:
        amount = input(f'Введите значение количества {i}-го товара:\n')
        if amount.isdigit():
            amount = int(amount)
            break
        else:
            print('Ошибка, необходимо ввести число:')
    cargo = (i, {"название": name, "цена": cost, "количество": amount, "eд": "шт."})
    data.insert(i - 1, cargo)
    if i == count:
        break
    i += 1

# data = [
#     (1, {"название": "компьютер", "цена": 20000, "количество": 5, "eд": "“шт.”"}),
#     (2, {"название": "принтер", "цена": 6000, "количество": 2, "eд": "“шт.”"}),
#     (3, {"название": "сканер", "цена": 2000, "количество": 7, "eд": "“шт.”"})
# ]

analytics_data = {}
for el_list in data:
    for key, val in el_list[1].items():
        analytics_data[key] = []

for el_list in data:
    for key, val in el_list[1].items():
        analytics_data[key].append(val)

# Костыль для исключения повторений в ключе единиц измерений
last = list(analytics_data.keys())[-1]
analytics_data[last] = list(set(analytics_data[last]))

print(data)
print(analytics_data)
