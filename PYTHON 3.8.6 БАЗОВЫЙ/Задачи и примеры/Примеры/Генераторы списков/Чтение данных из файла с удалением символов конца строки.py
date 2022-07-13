""" Чтение данных из файла
    с удалением символов конца строки
"""
# Функция open() открывает файл и
# создаёт итерируемый файловый объект.
# В цикле из этого объекта извлекаются
# строки и присваиваются переменной i.
# Метод strip() удаляет символ '\n' и т.п.
# Оставшаяся строка добавляется в список.
lines = [i.strip() for i in open("text.txt")]

# равносильно следующему:
# lines = []
# for i in open("text.txt"):
#     lines.append(i.strip())

print(lines)
# user@comp:~$ cat text.txt
# summer
# autumn
# winter
# spring
# user@comp:~$ python3 file.py
# ['summer', 'autumn', 'winter', 'spring']
