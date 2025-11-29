v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 0
for v4 in range(0, v1):
    if v4 + 1 == v2[v4]:
        v2[v4], v2[v4 + 1] = (v2[v4 + 1], v2[v4])
        v3 += 1
print(v3)
