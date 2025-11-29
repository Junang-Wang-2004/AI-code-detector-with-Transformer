v1, v2, v3 = map(int, input().split())
v4 = list(map(int, input().split()))
v5 = list(map(int, input().split()))
v6 = min(v4) + min(v5)
v7 = list(map(int, input().split()))
v8 = v7
for v9 in range(v3 - 1):
    v7 = v8
    v8 = list(map(int, input().split()))
    if v8[2] > v7[2]:
        v7 = v8
v10 = v4[v7[0] - 1] + v5[v7[1] - 1] - v7[2]
if v6 > v10:
    v6 = v10
print(v6)
