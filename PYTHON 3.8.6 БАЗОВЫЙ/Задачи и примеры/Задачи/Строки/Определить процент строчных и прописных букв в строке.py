""" Определить процент строчных и прописных букв в строке
    Вводится строка.
    Определить, сколько в ней строчных (малых)
    и сколько прописных (больших) букв.
    Результат выразить в процентах.
"""
string = input()

length = len(string)

# счётчики строчных и прописных букв
lower = 0
upper = 0

# Перебираем строку,
# по очереди извлекая каждый символ.
for i in string:

    # Строковые методы islower() и isupper()
    # проверяют, состоит ли строка
    # из символов нижнего регистра или
    # из символов верхнего регистра.
    # В данном случае
    # мы проверяем не целую строку,
    # а отдельно взятые символы.

    # Если символ нижнего регистра,
    if i.islower():
        # то увеличиваем счётчик строчных букв.
        lower += 1

    # Если символ верхнего регистра,
    elif i.isupper():
        # то увеличиваем счётчик прописных букв.
        upper += 1


# Вычисление процента строчных
# и прописных букв в строке.
per_lower = lower / length * 100
per_upper = upper / length * 100

print("Lower: %.2f%%" % per_lower)
print("Upper: %.2f%%" % per_upper)

# Примечание. Понятия верхнего и нижнего
# регистров имеют смысл только для букв.
# Остальные символы (например,
# знаки препинания) методы
# islower() и isupper() игнорируют.
