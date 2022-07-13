""" Преобразование текста в список слов
    с удалением знаков препинания
    Вводится строка, состоящая из слов
    и знаков препинания.
    Поместить слова из этой строки в список.
"""

string = input("Write down a text:\n")

# Знаки препинания,
# которые могут содержаться в тексте.
signs = ['.', ',', ':', ';',
         '!', '?', '(', ')']

# Метод split() без аргументов
# разделяет строку по символам пробела.
# Получаем список слов,
# которые могут начинаться или
# заканчиваться знаками препинания.
words = string.split()

# индекс текущего слова
i = 0

# извлекается каждое слово из списка
for word in words:

    # Если последний символ слова
    # содержится в списке знаков пунктуации,
    if word[-1] in signs:
        # то по индексу i в список
        # помещается копия этого слова,
        # но без последнего символа.
        # [:-1] обозначает взять срез
        # от начала до последнего элемента
        # (не включая последний).
        words[i] = word[:-1]
        # Заменяется значение 'word'
        # на текущее, иначе 'if' ниже
        # будет обрабатывать старое слово.
        word = words[i]

    # Если первый символ слова содержится
    # в списке знаков препинания,
    if word[0] in signs:
        # то переписать слово на его копию
        # без первого символа.
        # [1:] обозначает взять срез
        # от элемента с индексом 1
        # (второй элемент) до конца.
        words[i] = word[1:]

    # увеличение индекса
    i += 1

for i in words:
    print(i, end=' ')
print()

# Write down a text:
# one, two, three. Four? (five)
# one two three Four five
