from codewars_test import expect


def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')


test0 = expect(xo('Xo'), 'True expected')
test1 = expect(xo('xo0'), 'True expected')
test3 = expect(not xo('xxxoo'), 'False expected')
test4 = expect(xo('ooxXm'), 'True expected')
