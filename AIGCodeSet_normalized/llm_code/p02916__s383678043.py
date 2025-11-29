v1 = int(input())
v2 = []
v3 = []
v4 = []
for v5 in range(1, v1 + 1):
    v2 += [int(input())]
for v5 in range(1, v1 + 1):
    v3 += [int(input())]
for v5 in range(1, v1 + 1):
    v4 += [int(input())]
v6 = 0
for v5 in range(1, v1):
    if v2[v5] == v2[v5 - 1] + 1:
        v6 += v4[v5 - 1]
for v5 in range(1, v1 + 1):
    v6 += v3[v5 - 1]
print(v6)
