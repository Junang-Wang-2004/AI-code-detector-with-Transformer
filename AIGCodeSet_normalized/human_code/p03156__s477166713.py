v1 = int(input())
v2, v3 = map(int, input().split())
v4 = list(map(int, input().split()))
v5 = [0] * 3
for v6 in range(v1):
    if v4[v6] <= v2:
        v5[0] += 1
    elif v4[v6] <= v3:
        v5[1] += 1
    else:
        v5[2] += 1
print(min(v5))
