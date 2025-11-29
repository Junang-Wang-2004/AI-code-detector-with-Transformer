v1 = int(input())
v2 = list((int(x) for v3 in input().split()))
v4 = 0
for v5 in range(1, v1 - 1):
    if v2[v5 - 1] < v2[v5] and v2[v5] < v2[v5 + 1] or (v2[v5 + 1] < v2[v5] and v2[v5] < v2[v5 - 1]):
        v4 += 1
print(v4)
