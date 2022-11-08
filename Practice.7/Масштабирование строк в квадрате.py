from codewars_test import assert_equals


def scale(strng, k, v):
    if len(strng) == 0:
        return ""
    x = strng.split("\n")
    result = list()
    for item in x:
        q = ""
        d = list(item)
        for j in range(len(d)):
            q += d[j] * k
        result.extend([q] * v)
    return "\n".join(result)


def scale(strng, k, n):
    words = strng.split()
    words_h = ("".join(char * k for char in word) for word in words)
    return "\n".join("\n".join(word for _ in range(n)) for word in words_h)


test0 = assert_equals(
    scale("abcd\nefgh\nijkl\nmnop", 2, 3),
    "aabbccdd\naabbccdd\naabbccdd\neeffgghh\neeffgghh\neeffgghh\niijjkkll\niijjkkll\niijjkkll\nmmnnoopp\nmmnnoopp\nmmnnoopp",
)
test1 = assert_equals(scale("", 5, 5), "")
test2 = assert_equals(scale("Kj\nSH", 1, 2), "Kj\nKj\nSH\nSH")
