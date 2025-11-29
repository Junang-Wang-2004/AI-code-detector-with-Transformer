v1 = int(input())
v2 = [int(input()) for v3 in range(v1)]
if v2[0] != 0:
    print(-1)
    exit()
for v3 in range(v1 - 1):
    if v2[v3] < v2[v3 + 1] and v2[v3 + 1] - v2[v3] != 1:
        print(-1)
        exit()
    if v2[v3] > v3 + 1:
        print(-1)
        exit()
v4 = 0
v3 = 1
v5 = 0
while v3 != v1:
    if v2[v3] <= v5:
        v4 += v5
    v5 = v2[v3]
    v3 += 1
print(v4 + v2[-1])
