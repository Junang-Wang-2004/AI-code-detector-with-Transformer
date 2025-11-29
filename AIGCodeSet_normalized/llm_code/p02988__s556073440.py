v1 = 0
v2 = int(input())
v3 = list(map(int, input().split()))
for v4 in range(1, len(v3) - 1):
    if v3[v4 - 1] < v3[v4] < v3[v4 + 1] or v3[v4 + 1] < v3[v4] < v3[v4 - 1]:
        v1 += 1
print(v1)
