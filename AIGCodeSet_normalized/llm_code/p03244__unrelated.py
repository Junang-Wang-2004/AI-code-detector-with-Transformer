v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 0
for v4 in range(v1 // 2):
    if v2[2 * v4] != v2[2 * v4 + 2]:
        v3 += 1
print(v1 - v3)
