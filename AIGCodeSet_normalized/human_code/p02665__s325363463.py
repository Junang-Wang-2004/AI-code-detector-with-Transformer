v1 = int(input())
v2 = list(map(int, input().split()))
v3 = [1]
v4 = True
for v5 in range(v1 + 1):
    if v3[v5] < v2[v5]:
        v4 = False
        break
    elif v5 < v1:
        v3.append((v3[v5] - v2[v5]) * 2)
v6 = 0
if not v4:
    v6 = -1
else:
    v7 = 0
    for v5 in reversed(range(v1 + 1)):
        v6 += min(v2[v5] + v7, v3[v5])
        v7 += v2[v5]
print(v6)
