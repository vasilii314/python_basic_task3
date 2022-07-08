numbers = [0, 99, 100, 53, 44, 23, 4, 8, 16, 15, 77, 51]

for n in filter(lambda x: x > 50 and x % 2, numbers):
    print(n)
    