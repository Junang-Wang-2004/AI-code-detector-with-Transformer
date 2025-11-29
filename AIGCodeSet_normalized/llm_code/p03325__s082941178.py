v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 0
v4 = 0
while v4 < len(v2):
    if v2[v4] % 2 == 0:
        v3 += 1
        v2[v4] = int(v2[v4] // 2)
    v4 += 1
print(v3)
