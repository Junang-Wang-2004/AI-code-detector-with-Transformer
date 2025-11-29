v1 = int(input())
v2 = list(map(int, input().split()))

def f1(a1):
    v1 = v2 = 0
    for v3 in a1:
        v1 = max(v3, v1 + v3)
        v2 = max(v2, v1)
    return v2

def f2(a1):
    v1 = v2 = 0
    for v3 in a1:
        v1 = min(v3, v1 + v3)
        v2 = min(v2, v1)
    return v2
v3 = f1(v2[::2]) + f1(v2[1::2])
v4 = f2(v2[::2]) + f2(v2[1::2])
print(max(v3, v4))
