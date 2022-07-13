""" reverse(), sort() - переворот и сортировка списка
"""
a = [5, -1, 2, 0, 3, 1, 4]
print(a, "origin")

a.reverse()
print(a, "reverse")

a.sort()
print(a, "sort")

a.sort(reverse=True)
print(a, "reverse sort")

b = [(3, 4), (5, 2), (2, 3), (0, 9)]
print(b, "origin")
b.sort()
print(b, "sort by first item")

def item_two_of_tuple(t):
    return t[1]

b.sort(key=item_two_of_tuple)
print(b, "sort by second item")

# [5, -1, 2, 0, 3, 1, 4] origin
# [4, 1, 3, 0, 2, -1, 5] reverse
# [-1, 0, 1, 2, 3, 4, 5] sort
# [5, 4, 3, 2, 1, 0, -1] reverse sort
# [(3, 4), (5, 2), (2, 3), (0, 9)] origin
# [(0, 9), (2, 3), (3, 4), (5, 2)] sort by first item
# [(5, 2), (2, 3), (3, 4), (0, 9)] sort by second item
