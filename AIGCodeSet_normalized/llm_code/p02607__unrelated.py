v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 0
for v4 in range(v1):
    if (v4 + 1) % 2 == 1 and v2[v4] % 2 == 1:
        v3 += 1
print(v3)
