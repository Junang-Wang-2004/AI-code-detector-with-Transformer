v1 = lambda n: 2 ** (n + 1) - 1
v2 = lambda n: 2 ** (n + 2) - 3

def f1(a1, a2):
    if a1 == 0:
        return 0 if a2 <= 0 else 1
    if a2 <= 1 + v2(a1 - 1):
        return f1(a1 - 1, a2 - 1)
    else:
        return v1(a1 - 1) + 1 + f1(a1 - 1, a2 - 2 - v2(a1 - 1))
v3, v4 = map(int, input().split())
print(f1(v3, v4))
