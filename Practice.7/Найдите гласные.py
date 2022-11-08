from codewars_test import assert_equals


def vowel_indices(word):
    vowels = ["a", "e", "i", "o", "u", "y", "Y", "A", "E", "I", "O", "U"]
    vowelsList = []
    for index, letter in enumerate(word):  # добавить индекс с перечислением
        if letter in vowels:
            vowelsList.append(
                index + 1
            )  # добавить 1, так как список/массивы начинаются с 0
    return vowelsList
    # return [i for i, x in enumerate(word, 1) if x.lower() in 'aeiouy']
    # return [i+1 for i,c in enumerate(word.lower()) if c in 'aeiouy']


test = assert_equals(vowel_indices("mmm"), [], "failed on the word 'mmm'")
test1 = assert_equals(vowel_indices("apple"), [1, 5], "failed on the word 'apple'")
test2 = assert_equals(vowel_indices("123456"), [], "failed on the word '123456'")
test3 = assert_equals(
    vowel_indices("UNDERARMED"),
    [1, 4, 6, 9],
    "failed on the word 'UNDERARMED'. Consider case",
)
