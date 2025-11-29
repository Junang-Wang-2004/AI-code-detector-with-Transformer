v1 = int(input())
v2 = int(input())
v3 = 0
for v4 in range(v1):
    v5, v6 = map(int, input().split())
    if v2 * v2 >= v5 * v5 + v6 * v6:
        v3 += 1
print(v3)
