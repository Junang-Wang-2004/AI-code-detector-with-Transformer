v1 = int(input())
v2 = list(map(int, input().split()))
if 1 not in v2:
    print(-1)
    exit()
v3 = 0
v4 = 1
for v5 in range(v1):
    if v2[v5] != v4:
        v3 += 1
    else:
        v4 += 1
print(v3)
