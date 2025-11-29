v1, v2 = [int(x) for v3 in input().split(' ')]
v4 = [int(v3) for v3 in input().split(' ')]
v4.sort(reverse=True)
for v5 in range(v2):
    v6, v7 = [int(v3) for v3 in input().split(' ')]
    for v8 in range(min(v6, v1)):
        if v4[v8] < v7:
            v4[v8] = v7
        else:
            break
    v4.sort(reverse=True)
print(sum(v4))
