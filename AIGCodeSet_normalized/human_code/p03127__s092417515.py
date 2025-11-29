import copy
v1 = int(input())
v2 = list(map(int, input().split()))
v3 = copy.deepcopy(v2)
while max(v2) != min(v2):
    v4 = min(v2)
    for v5 in range(v1):
        if v2[v5] % v4 == 0:
            v2[v5] = v4
        else:
            v2[v5] = v2[v5] % v4
print(min(v2))
