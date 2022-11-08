""" Запись в текстовый файл
    Используя методы "write" и "writelines"
    запишите в файл строки и список.
    Откройте файл на чтение и выведите его содержимое на экран.
"""

# режим 'w' открывает файл на запись
f = open("newfile.txt", "w")

# метод write() записывает строку
f.write("One")
f.write("Two")

# В метод writelines() можно передать
# как строку, ...
f.writelines("Three")

lst = ["Four", "Five"]

# ... так и последовательность строк.
f.writelines(lst)

f.close()

f = open("newfile.txt")
print(f.read())
f.close()
# OneTwoThreeFourFive
