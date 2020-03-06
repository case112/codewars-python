# Yor task is to write function factorial

# https://en.wikipedia.org/wiki/Factorial


def factorial(n):
    res = 1
    if n == 0:
        return 1
    if n == 1:
        return 1
    for x in range(n+1):
        if x > 0:
            res = res * x
            print(res)
    return res