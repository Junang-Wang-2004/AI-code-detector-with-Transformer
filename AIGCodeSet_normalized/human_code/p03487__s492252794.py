v1 = int(input())
v2 = list(map(int, input().strip().split()))
v3 = {}
for v4 in range(v1):
    if v3.get(v2[v4]) == None:
        v3[v2[v4]] = 1
    else:
        v3[v2[v4]] += 1
v5 = 0
for v6 in v3.keys():
    if v6 > v3[v6]:
        v5 += v3[v6]
    else:
        v5 += v3[v6] - v6
print(v5)
