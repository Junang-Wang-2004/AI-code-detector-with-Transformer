import sys
input = sys.stdin.readline
v1, v2, v3 = map(int, input().split())
v4 = [int(input()) for v5 in range(v1)]
v6 = -1
v7 = pow(10, 10)
while v7 - v6 > 1:
    v8 = v6 + (v7 - v6) // 2
    v9 = v8
    for v5 in range(v1):
        if v8 * v3 >= v4[v5]:
            continue
        else:
            v10 = -(-(v4[v5] - v8 * v3) // (v2 - v3))
            v9 -= v10
            if v9 < 0:
                break
    if v9 >= 0:
        v7 = v8
    else:
        v6 = v8
print(v7)
