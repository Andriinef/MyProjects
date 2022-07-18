import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
d = {}

for i in lst_in:
    value, key = i.split()
    if key in d:
        d[key] += [value]
    else:
        d[key] = [value]

print(*sorted(d.items()))
# test 2
