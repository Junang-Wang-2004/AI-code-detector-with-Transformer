v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = list(map(int, input().split()))
v3.sort()
v4.sort(reverse=True)

def f1(a1):
    v1 = 0
    for v2, v3 in zip(v3, v4):
        v4 = a1 // v3
        if v4 >= v2:
            continue
        v1 += v2 - v4
    if v1 <= v2:
        return True
    return False
v5 = 0
v6 = v3[-1] * v4[0]
while v5 < v6:
    v7 = (v5 + v6) // 2
    if f1(v7):
        v6 = v7
    else:
        v5 = v7 + 1
print(v5)
