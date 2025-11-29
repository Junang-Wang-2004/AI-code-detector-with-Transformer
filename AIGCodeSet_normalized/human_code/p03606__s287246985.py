v1 = int(input())
v2 = 0
for v3 in range(v1):
    v4, v5 = map(int, input().split())
    v2 += v5 - v4 + 1
print(v2)
