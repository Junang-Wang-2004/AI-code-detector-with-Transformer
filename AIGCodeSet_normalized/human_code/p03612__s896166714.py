v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 0
v4 = 0
for v5 in range(v1):
    if v5 + 1 != v2[v5]:
        v3 += (v4 + 1) // 2
        v4 = 0
    else:
        v4 += 1
v3 += (v4 + 1) // 2
print(v3)
