v1 = int(input())
if v1 == 1:
    print(0)
elif v1 == 2:
    print(2)
else:
    print(2 * 10 ** (v1 - 2) % (10 ** 9 + 7))
