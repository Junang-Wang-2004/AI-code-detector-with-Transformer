v1 = int(input())
v2 = list(map(int, input().split()))
v3 = list(map(int, input().split()))
v4 = list(map(int, input().split()))
v2 = [d - 1 for v5 in v2]
v6 = 0
v7 = v2[0]
for v8 in v2:
    v6 = v6 + v3[v8]
    if v7 + 1 == v8:
        v6 += v4[v8 - 1]
    v7 = v8
print(v6)
