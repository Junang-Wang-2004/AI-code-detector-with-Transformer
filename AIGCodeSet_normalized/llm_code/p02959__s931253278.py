v1 = int(input())
v2 = [int(i) for v3 in input().split()]
v4 = [int(v3) for v3 in input().split()]
v5 = [0] * v1
v6 = 0
for v3 in range(0, v1):
    if int(v4[v3]) - int(v2[v3]) >= 0:
        v6 = v6 + int(v2[v3])
        v4[v3 + 1] = int(v4[v3 + 1]) - (int(v4[v3]) - int(v2[v3]))
    else:
        v6 = v6 + int(v4[v3])
if int(v2[v1]) - int(v4[v1 - 1]) > 0:
    v6 = v6 + (int(v2[v1]) - int(v4[v1 - 1]))
else:
    v6 = v6 + int(v4[v1 - 1])
print(v6)
