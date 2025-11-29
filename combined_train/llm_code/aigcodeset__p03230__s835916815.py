v1 = int(input())
v2 = (v1 - 2) ** 0.5
if v1 == 3:
    print('Yes')
    v3 = [2, 1, 2]
    print(*v3)
    v3 = [2, 2, 3]
    print(*v3)
    v3 = [2, 3, 1]
    print(*v3)
    exit()
if v2 % 1 != 0:
    print('No')
    exit()
v2 = int(v2)
v4 = []
for v5 in range(v2):
    v6 = [1] + [2 + j + v2 * v5 for v7 in range(v2)]
    v4.append(v6)
for v5 in range(v2):
    v6 = [2 + v5 + v2 * v7 for v7 in range(v2)] + [v1]
    v4.append(v6)
print('Yes')
for v8 in v4:
    v9 = [len(v8)] + v8
    print(*v9)
