v1 = int(input())
v2 = list(map(int, input().split()))
v3 = list(set(v2))
v3.sort()
v4 = []
for v5 in v3:
    v4.append(v2.count(v5))
v6 = 0
v7 = 0
while v7 <= len(v3) - 3:
    v8 = v7 + 1
    while v8 <= len(v3) - 2:
        v9 = v8 + 1
        while v9 <= len(v3) - 1:
            if v3[v7] + v3[v8] > v3[v9]:
                v6 += v4[v7] * v4[v8] * v4[v9]
            v9 += 1
        v8 += 1
    v7 += 1
print(v6)
