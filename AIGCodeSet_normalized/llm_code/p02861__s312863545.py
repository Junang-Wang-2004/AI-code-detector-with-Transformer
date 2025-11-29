import math
v1 = int(input())
v2 = {}
for v3 in range(v1):
    v4, v5 = map(int, input().split())
    v2[v3] = (v4, v5)
v6 = []
for v3 in range(v1):
    for v7 in range(v3 + 1, v1):
        v8, v9 = v2[v3]
        v10, v11 = v2[v7]
        v12 = math.sqrt((v8 - v10) ** 2 + (v9 - v11) ** 2)
        v6.append(v12)
sum = 0
for v3 in range(len(v6)):
    sum += v6[v3]
print(math.factorial(v1 - 1) * 2 * sum / math.factorial(v1))
