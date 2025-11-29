v1, v2 = map(int, input().split())
v3 = v2 - v1

def f1(a1):
    if a1 == 0:
        return 0
    else:
        return a1 + f1(a1 - 1)
print(f1(v3) - v2)
