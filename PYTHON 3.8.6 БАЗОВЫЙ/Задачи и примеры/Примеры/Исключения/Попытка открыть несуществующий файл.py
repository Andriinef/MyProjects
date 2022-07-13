""" Попытка открыть несуществующий файл
"""

f_name = input("File: ")

try:
    # Если файла не существует,
    # то будет сгенерировано исключение
    # FileNotFoundError.
    f = open(f_name)
# Здесь мы перехватываем это исключение.
except FileNotFoundError:
    print("Error. No this file!")
# Ветка 'else' сработает,
# если не сработал ни один 'except'.
else:
    # Читать файл имеет смысл,
    # только если он был успешно открыт.
    print(f.read())
# File: dfa.txt
# Error. No this file!
