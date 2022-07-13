""" In a small town the population is p0 = 1000 at the beginning of a year.
    The population regularly increases by 2 percent per year and moreover 50
    new inhabitants per year come to live in the town.
    How many years does the town need to see its population
    greater or equal to p = 1200 inhabitants?
"""
from codewars_test import assert_equals


def nb_year(p0, percent, aug, p):
    # po - population
    # percent - population regularly increases
    # aug - inhabitants coming or leaving each year
    # p - population to surpass
    year = 0
    while p0 < p:
        p0 += int(p0 * percent/100) + aug
        year += 1
    return year
    # if p0 < p:
    #     return nb_year(p0 + int(p0 * percent / 100) + aug, percent, aug, p, years + 1)
    # return years


test = assert_equals(nb_year(1500, 5, 100, 5000), 15)
test1 = assert_equals(nb_year(1500000, 2.5, 10000, 2000000), 10)
test2 = assert_equals(nb_year(1500000, 0.25, 1000, 2000000), 94)