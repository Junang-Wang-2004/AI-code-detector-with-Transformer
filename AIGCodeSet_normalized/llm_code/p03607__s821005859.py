v1 = int(input())
v2 = []
for v3 in range(0, v1):
    v4 = int(input())
    v2.append(v4)
v5 = set(v2)
v6 = [v2.count(v3) for v3 in v5]
print(sum([1 for v3 in v6 if v3 % 2 == 1]))
