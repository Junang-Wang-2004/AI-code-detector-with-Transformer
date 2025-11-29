import copy
v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 10 ** 9 + 7
v4 = copy.deepcopy(v2)
v5 = v2[v1 - 1]
for v6 in range(v1 - 2, -1, -1):
    v5 = int((v5 + v2[v6]) % v3)
    v4[v6] = v5
v7 = 0
for v8 in range(v1 - 1):
    v7 = (v7 + v2[v8] * v4[v8 + 1] % v3) % v3
print(int(v7))
