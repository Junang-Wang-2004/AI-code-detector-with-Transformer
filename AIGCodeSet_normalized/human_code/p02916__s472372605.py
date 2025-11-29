v1 = -1
v2 = int(input())
v3 = list(map(int, input().split()))
v4 = list(map(int, input().split()))
v5 = [0] + list(map(int, input().split()))
v6 = 0
v7 = 0
for v8, v9 in zip(v3, v4):
    v6 += v9
    if v1 + 1 == v8:
        v6 += v5[v1]
    v1 = v8
print(v6)
