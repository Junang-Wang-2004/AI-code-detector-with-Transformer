import copy
v1, v2 = map(int, input().split())
v3 = sorted(list(map(int, input().split())))
v4 = []
for v5 in range(v2):
    v6 = copy.deepcopy(v3)
    v7, v8 = map(int, input().split())
    del v6[0:v7]
    v4.append(sum([sum(v6), sum([v8] * v7)]))
print(max(v4))
