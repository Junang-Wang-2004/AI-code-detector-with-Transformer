v1, v2 = map(int, input().split())
v3 = []
v4 = []
for v5 in range(v2):
    v3.append(int(input()))
    v4.append(list(map(int, input().split())))
v6 = [0] * v1
for v7 in v4:
    for v8 in range(len(v7)):
        v6[v7[v8] - 1] += 1
v9 = 0
for v10 in v6:
    if v10 == 0:
        v9 += 1
print(v9)
