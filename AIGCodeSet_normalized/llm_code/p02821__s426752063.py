v1, v2 = map(int, input().split())
v3 = [10 ** 18] + sorted(map(int, input().split()), reverse=True)

def f1(a1):
    v1 = 0
    v2 = v1
    for v3 in range(1, v1 + 1):
        while v3[v3] + v3[v2] < a1:
            v2 -= 1
        v1 += v2
    return v1
v4, v5 = (0, 10 ** 18)
while v4 < v5 - 1:
    v6 = (v4 + v5) // 2
    if f1(v6) >= v2:
        v4 = v6
    else:
        v5 = v6
v7 = [0] * (v1 + 1)
for v8 in range(v1):
    v7[v8 + 1] = v7[v8] + v3[v8 + 1]
v9 = 0
v10 = v1
for v8 in range(1, v1 + 1):
    while v3[v8] + v3[v10] < v4 + 1:
        v10 -= 1
    v9 += v3[v8] * v10 + v7[v10]
    v2 -= v10
if v2:
    v9 += v4 * v2
print(v9)
