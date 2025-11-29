def f1(a1, a2):
    if a1 == 0:
        return 1 if a2 >= 1 else 0
    elif a2 <= 2 ** (a1 - 1):
        return f1(a1 - 1, a2)
    elif a2 <= 2 ** a1 + 2 ** (a1 - 1):
        return 2 ** (a1 - 1) + f1(a1 - 1, a2 - 2 ** a1)
    else:
        return 2 ** a1 + f1(a1 - 1, a2 - 2 ** a1 - 2 ** (a1 - 1))
v1, v2 = map(int, input().split())
print(f1(v1, v2))
