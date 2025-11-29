v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = list(map(int, input().split()))
v3.sort()
v4.sort(reverse=True)
v5, v6 = (-1, v3[1] * v4[-1])
while v6 - v5 > 1:
    v7 = (v5 + v6) // 2
    v8 = 0
    for v9 in range(v1):
        v8 += max(0, v3[v9] - v7 // v4[v9])
    if v8 <= v2:
        v6 = v8
    else:
        v5 = v8
print(v6)
