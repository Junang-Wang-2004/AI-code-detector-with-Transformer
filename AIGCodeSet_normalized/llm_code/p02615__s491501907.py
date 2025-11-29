v1 = int(input())
v2 = sorted([int(i) for v3 in input().split()])[::-1]
v4 = [v2[0], v2[1]]
v5 = v2[0]
for v3 in range(v1 - 2):
    v5 += min(v4[0], v4[1])
    v4 = v4[:1]
    v4 += [v2[v3 + 2]]
print(v5)
