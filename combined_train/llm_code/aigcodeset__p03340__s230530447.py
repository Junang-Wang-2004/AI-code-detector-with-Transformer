v1 = int(input())
v2 = list(map(int, input().split()))
v3 = []
for v4 in range(v1):
    v3.append(v2[v4])
v4 = 1
v5 = 0
v6 = v3[0]
v7 = v1
v8 = 0
while v4 < v1 - 1 or v5 < v1 - 1:
    if v3[v5] ^ v3[v4] == v3[v5] | v3[v4]:
        v6 = v3[v5] | v3[v4]
        v8 += 1
        v7 += v8
        v4 += 1
    else:
        v6 -= v3[v5]
        v5 += 1
print(v7)
