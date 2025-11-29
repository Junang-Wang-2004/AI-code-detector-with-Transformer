import math
v1, v2 = map(int, input().split())
v3 = [list(map(int, input().split())) for v4 in range(v1)]
sum = 0
for v5 in range(v1):
    if v2 >= math.sqrt(v3[v5][0] ** 2 + v3[v5][1] ** 2):
        sum += 1
print(sum)
