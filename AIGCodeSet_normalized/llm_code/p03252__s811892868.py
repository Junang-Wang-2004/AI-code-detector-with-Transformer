from collections import defaultdict
v1, v2 = map(lambda x: x.strip(), open(0).read().split())
v3, v4 = (defaultdict(str), defaultdict(str))
v5 = 'Yes'
for v6, v7 in zip(v1, v2):
    if v3[v6] and v3[v6] != v7:
        v5 = 'No'
        break
    v3[v6] = v7
    if v4[v7] and v4[v7] != v6:
        v5 = 'No'
        break
    v4[v7] = v6
print(v5)
