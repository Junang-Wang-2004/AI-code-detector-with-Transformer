v1 = int(input())
v2 = sorted(list(map(int, input().split())))
v3 = v2[0]
for v4 in range(1, v1):
    v3 = (v3 + v2[v4]) / 2
print(v3)
