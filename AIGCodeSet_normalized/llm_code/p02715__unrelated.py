def f1(a1, a2):
    while a2:
        a1, a2 = (a2, a1 % a2)
    return a1

def f2(a1, a2):
    v1 = 10 ** 9 + 7
    v2 = 0
    for v3 in range(1, a2 + 1):
        v2 += pow(a2 // v3, a1, v1) * v3 % v1
    return v2 % v1
v1, v2 = map(int, input().split())
print(f2(v1, v2))
