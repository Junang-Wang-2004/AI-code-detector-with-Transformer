v1 = str(input())
v2 = len(v1)
v3 = 0
v4 = []
for v5 in range(v2):
    for v6 in range(v5 + 1, v2):
        v7 = v1[v5:v6 + 1]
        v4.append(v1[:v5] + v7[::-1] + v1[v6 + 1:])
        if v1[v5:v6 + 1] == v7[::-1]:
            v3 += 1
print(1 + v2 * (v2 - 1) // 2 - v3)
v4.sort()
print(v4)
print(len(set(v4)))
