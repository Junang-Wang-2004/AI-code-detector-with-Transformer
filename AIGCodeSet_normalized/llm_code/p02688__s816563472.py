v1, v2 = list(map(int, input().split()))
v3 = [0] * v1
for v4 in range(v2):
    v5 = list(map(int, input().split()))
    for v6 in range(1, len(v5)):
        v3[v5[v6] - 1] = 1
print(sum(v3))
