v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 0
for v4 in range(v1):
    while v2[v4] % 2 == 0 and v2[v4] > 0:
        v3 += 1
        v2[v4] //= 2
print(v3)
