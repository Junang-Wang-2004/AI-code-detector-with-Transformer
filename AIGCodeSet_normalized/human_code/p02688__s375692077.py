v1, v2 = map(int, input().split())
v3 = [0] * v1
for v4 in range(v2):
    v5 = int(input())
    for v6 in [int(x) for v7 in input().split()]:
        v3[v6 - 1] += 1
print(sum([1 for v8 in v3 if v8 == 0]))
