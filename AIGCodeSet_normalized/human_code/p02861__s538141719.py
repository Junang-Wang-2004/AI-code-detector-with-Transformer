import math
v1 = int(input())
v2 = []
v3 = math.factorial(v1)
for v4 in range(v1):
    v5, v6 = list(map(int, input().split()))
    v2.append([v5, v6])
v7 = []

def f1(a1, a2):
    if len(a2) == v1:
        return v7.append(a2)
    for v1 in range(len(a1)):
        f1(a1[:v1] + a1[v1 + 1:], a2 + [a1[v1]])
f1(v2, [])
v8 = 0
for v9 in range(len(v7)):
    for v10 in range(len(v7[v9]) - 1):
        v8 += math.sqrt((v7[v9][v10][0] - v7[v9][v10 + 1][0]) ** 2 + (v7[v9][v10][1] - v7[v9][v10 + 1][1]) ** 2)
print(v8 / v3)
