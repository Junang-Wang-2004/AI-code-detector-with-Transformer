v1 = int(input())
v2 = 0
v3 = 0
for v4 in range(v1):
    v3, v5 = map(int, input().split())
    v6 = v3 % v5
    if v6 != 0:
        v7 = v5 - v6
        v2 += v7
        v3 -= v7
    v8 = v3 // v5
    v2 += v8
print(v2)
