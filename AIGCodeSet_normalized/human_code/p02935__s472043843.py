v1 = int(input())
v2 = [int(_) for v3 in input().split()]
v2.sort()
v4 = v2[0]
for v5 in range(v1 - 1):
    v4 = (v4 + v2[v5 + 1]) / 2
print(v4)
