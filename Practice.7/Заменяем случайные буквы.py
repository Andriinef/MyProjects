from codewars_test import assert_equals


def uncensor(infected, discovered):
    if len(discovered) == 0:
        infected = infected.replace("*", "")
    for item in range(len(discovered)):
        infected = infected.replace("*", discovered[item], 1)
    return infected

    # return infected.replace('*', '{}').format(*discovered)


""" * при использовании внутри функции означает, 
    что переменная, следующая за *, 
    является итерируемой и извлекается внутри этой функции
"""

test0 = assert_equals(
    uncensor("*h*s *s v*ry *tr*ng*", "Tiiesae"), "This is very strange"
)
test1 = assert_equals(uncensor("A**Z*N*", "MAIG"), "AMAZING")
test2 = assert_equals(uncensor("xyz", ""), "xyz")
test3 = assert_equals(uncensor("***", ""), "")
test4 = assert_equals(uncensor("***", "abc"), "abc")
