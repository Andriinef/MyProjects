""" Чтение методом readlines()
Прочитайте содержимое файла методом "readlines". Выведите результат на экран.
"""

f = open("text.txt")

# Метод readlines() без аргументов
# читает все строки файла и
# создаёт из них список.
text = f.readlines()

f.close()

print(text)
# ['one two\n', 'town city\n', 'big small']
