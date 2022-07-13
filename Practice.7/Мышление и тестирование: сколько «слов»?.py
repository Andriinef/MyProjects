from codewars_test import assert_equals


def testit(s):
    counter = 0
    word = list('word')     # возвращает список
    for letter in s.lower():        # преобразует все символы верхнего регистра в строке в символы нижнего регистра и возвращает их.
        if letter == word[0]:
            word.pop(0)    # удаляет элемент с заданным индексом из списка и возвращает удаленный элемент.
            if len(word) == 0:
                counter += 1
                word = list('word')
    return counter


# def testit(s):
#     new = ""
#     count = 0
#     for i in s.lower():
#         if i == "w" and new == "":
#             new += "w"
#         if i == "o" and new == "w":
#             new += "o"
#         if i == "r" and new == "wo":
#             new += "r"
#         if i == "d" and new == "wor":
#             new = ""
#             count += 1
#     return count


test0 = assert_equals(testit("word"), 1)
test1 = assert_equals(testit("hello world"), 1)
test2 = assert_equals(testit("I love codewars."), 0)
test3 = assert_equals(testit("My cat waiting for a dog."), 1)
test4 = assert_equals(testit("We often read book, a word hidden in the book."), 2)
test5 = assert_equals(testit("When you in order to do something by a wrong way, your heart will missed somewhere."), 2)
test6 = assert_equals(testit("This sentence has one word."), 1)
test7 = assert_equals(testit("This sentence has two words, not one word."), 2)
test8 = assert_equals(testit("One word + one word = three words -)"), 3)
test9 = assert_equals(testit("Can you find more word for me?"), 1)