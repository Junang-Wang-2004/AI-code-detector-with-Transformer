v1 = int(input())
v2 = []
for v3 in range(v1):
    v2.append(int(input()))
v2.sort()
v4 = v2[v1 - 1]
v5, v6 = ([], [])
v7 = 1
for v3 in range((v1 - 1) // 2):
    if v7:
        v5.append(v2[v3])
        v6.append(v2[v1 - v3 - 2])
        v7 = 0
    else:
        v5.append(v2[v1 - v3 - 1])
        v6.append(v2[v3])
        v7 = 1
if (v1 - 1) % 2 == 1:
    v5.append(v2[v1 // 2])
v8 = v4 - v5[0] + v4 - v6[0]
for v3 in range(1, len(v5)):
    v8 += abs(v5[v3] - v5[v3 - 1])
for v3 in range(1, len(v6)):
    v8 += abs(v6[v3] - v6[v3 - 1])
v4 = v2[0]
v5, v6 = ([], [])
v7 = 1
for v3 in range((v1 - 1) // 2):
    if v7:
        v5.append(v2[v1 - v3 - 1])
        v6.append(v2[v1 - v3 - 2])
        v7 = 0
    else:
        v5.append(v2[v3])
        v6.append(v2[v1 - v3 - 1])
        v7 = 1
if (v1 - 1) % 2 == 1:
    v5.append(v2[v1 // 2])
v9 = v5[0] - v4 + v6[0] - v4
for v3 in range(1, len(v5)):
    v9 += abs(v5[v3] - v5[v3 - 1])
for v3 in range(1, len(v6)):
    v9 += abs(v6[v3] - v6[v3 - 1])
print(max(v8, v9))
