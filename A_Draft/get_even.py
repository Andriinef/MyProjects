def get_even(x):
    return x % 3 == 0


for item in range(1, int(input("Enter an integer: "))):
    if get_even(item):
        print(item)
