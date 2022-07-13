""" Товары с ценой и количеством
    Дан словарь, в котором ключами являются товары,
    а значениями - списки,
    состоящие из цены и количества товара.
    Напишите программу, которая эмулирует
    процесс покупки одним пользователем нескольких товаров,
    при этом их количество в словаре должно уменьшаться.
    В конце на экран должна выводиться
    общая сумма покупки и словарь.
"""

goods = {"Apple": [4.5, 10],
         "Orange": [6.2, 5],
         "Pineapple": [10.0, 1],
         "Mango": [7.5, 2],
         "Banana": [3.8, 10]}

# В переменную  'value' записывается список,
# первый элемент которого обозначает цену,
# а второй - количество.
for key, value in goods.items():
    print(key, '-', value[0], '-', value[1])

# общая стоимость покупки
cost = 0

while True:

    # товар и его количество
    good = input("What? (n - nothing) ")
    if good == 'n':
        break
    qty = int(input("How many? "))

    # Если было введено больше количества,
    # чем имеется,
    # то текущая итерация цикла завершается.
    if qty > goods[good][1]:
        print("We don't have so much.")
        continue

    # Вычисляется цена количества
    # указанного товара
    # и добавляется к общей сумме.
    cost += goods[good][0] * qty

    # Уменьшается количество
    # этого товара в словаре.
    goods[good][1] -= qty

print("Price:", cost)

for key, value in goods.items():
    print(key, '-', value[0], '-', value[1])

# Apple - 4.5 - 10
# Orange - 6.2 - 5
# Pineapple - 10.0 - 1
# Mango - 7.5 - 2
# Banana - 3.8 - 10
# What? (n - nothing) Banana
# How many? 5
# What? (n - nothing) Mango
# How many? 2
# What? (n - nothing) Orange
# How many? 6
# We don't have so much.
# What? (n - nothing) n
# Price: 34.0
# Apple - 4.5 - 10
# Orange - 6.2 - 5
# Pineapple - 10.0 - 1
# Mango - 7.5 - 0
# Banana - 3.8 - 5
