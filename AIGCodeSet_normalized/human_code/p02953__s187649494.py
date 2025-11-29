v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 'Yes'
v4 = max(0, v2[0] - 1)
for v5 in range(1, v1):
    if v2[v5] < v4:
        v3 = 'No'
        break
    v4 = max(v4, max(0, v2[v5] - 1))
print(v3)
