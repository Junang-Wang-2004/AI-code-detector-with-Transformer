def f1(a1):
    v1 = 0
    for v2 in A:
        v1 += (v2 - 1) // a1
    if v1 <= k:
        return True
    else:
        return False

def f2(a1, a2):
    while abs(a2 - a1) > 1:
        v1 = (a2 + a1) // 2
        if f1(v1):
            a2 = v1
        else:
            a1 = v1
    return a2
v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
print(f2(0, max(v3) + 1))
