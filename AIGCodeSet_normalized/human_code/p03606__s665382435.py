v1 = int(input())
v2 = [list(map(int, input().split())) for v3 in range(v1)]
v4 = 0
for v3 in v2:
    v4 += v3[1] - v3[0] + 1
print(v4)
