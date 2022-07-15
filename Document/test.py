x, y = 5, 4
a, b, c = [], [], []
for i in range(x):
    a.append(i)
    for j in range(y):
        b.append(j)
        c.append(i)
print(a)
print(b)
print(c)
