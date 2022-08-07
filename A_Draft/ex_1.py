cities = ["Москва", "Ульяновск", "Самара", "Уфа", "Омск", "Тула"]
gen = (x for i in range(1000000) for x in cities)
k = 20
for i in range(k):
    print(next(gen), end=' ')
