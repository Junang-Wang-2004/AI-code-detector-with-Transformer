v1 = int(input())
v2 = list(map(int, input().split()))
v3 = list(map(int, input().split()))
v4 = [0] * (v1 + 1)
v5 = 0
for v6 in range(v1):
    if v3[v6] + v4[v6] > v2[v6]:
        if v4[v6] >= v2[v6]:
            v5 = v5 + v2[v6]
            v4[v6 + 1] = v3[v6]
        else:
            v5 = v5 + v2[v6]
            v4[v6 + 1] = v3[v6] + v4[v6] - v2[v6]
    else:
        v5 = v5 + v3[v6] + v4[v6]
if v4[v1] > v2[v1]:
    v5 = v5 + v2[v1]
else:
    v5 = v5 + v4[v1]
print(v5)
