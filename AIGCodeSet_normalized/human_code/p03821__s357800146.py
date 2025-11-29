v1 = int(input())
v2, v3 = ([], [])
for v4 in range(v1):
    v5, v6 = map(int, input().split())
    v2.append(v5)
    v3.append(v6)
v7 = 0
for v4 in range(v1):
    v5, v6 = (v2[-(v4 + 1)], v3[-(v4 + 1)])
    v7 += ((v5 + v7 - 1) // v6 + 1) * v6 - (v5 + v7)
print(v7)
