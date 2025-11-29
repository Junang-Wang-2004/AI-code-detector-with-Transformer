v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 0
for v4 in v2:
    v3 += v4 - 1
print(v3)
