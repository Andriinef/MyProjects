""" Если вводится строка, а не число, как ожидается
"""
n = input("Enter a number: ")

# Цикл завершится только тогда,
# когда значение переменной будет
# успешно преобразовано в тип float.
while type(n) != float:
    try:
        # пытаемся преобразовать
        n = float(n)

    # Если значение 'n' невозможно преобразовать
    # в float, то возникает исключение ValueError.
    except ValueError:
        print("Input error!")
        # снова запрашиваем ввод
        n = input("Enter a number: ")

print(n / 2)
# Enter a number: 4j
# Input error!
# Enter a number: 2.3
# 1.15
