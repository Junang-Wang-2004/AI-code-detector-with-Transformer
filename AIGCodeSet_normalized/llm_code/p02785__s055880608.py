v1, v2 = map(int, input().split())
v3 = [int(i) for v4 in input().split()]
v3.sort()
v5 = 0
for v4 in range(v1 - v2, v1):
    v5 += v3[v4]
if v2 >= v1:
    v6 = 0
else:
    v3.sort()
    v5 = 0
    for v4 in range(v1 - v2, v1):
        v5 += v3[v4]
    v6 = sum(v3) - v5
print(v6)
