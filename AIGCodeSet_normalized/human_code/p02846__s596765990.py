v1, v2 = map(int, input().split())
v3, v4 = map(int, input().split())
v5, v6 = map(int, input().split())
v7 = (v5 - v3) * v1
v8 = (v6 - v4) * v2
if v7 * v8 > 0 or abs(v7) > abs(v8):
    print(0)
elif abs(v7) == abs(v8):
    print('infinity')
else:
    v9 = abs(v7) // abs(v7 + v8)
    while (v9 + 1) * abs(v7 + v8) <= abs(v7):
        v9 += 1
    v10 = 2 * v9
    if abs(v7) % abs(v7 + v8) != 0:
        v10 += 1
    print(v10)
