v1, v2, v3 = map(int, input().split())
v4 = [int(input()) for v5 in range(v1)]
v6 = int(1000000000.0)
v7, v8, v9 = (0, v6 // 2, v6 + 1)

def f1(a1):
    global N, A, B
    v1 = v2 - v3
    v2 = a1
    for v3 in v4:
        v4 = v3 - v3 * a1
        if v4 > 0:
            v2 -= (v4 + v1 - 1) // v1
    return v2 >= 0
while v9 - v7 > 1:
    if f1(v8):
        v9 = v8
    else:
        v7 = v8
    v8 = (v9 + v7 + 1) // 2
print(v8)
