v1 = int(input())
v2 = list(map(int, input()))
v3 = 0
for v4 in range(1, v1):
    if v2[v4] == v2[v4 - 1]:
        v3 += 1
print(v3)
