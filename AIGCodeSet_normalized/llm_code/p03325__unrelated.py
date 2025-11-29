v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 0
for v4 in range(v1):
    while v2[v4] % 2 == 0:
        v2[v4] //= 2
        v3 += 1
print(v3)
