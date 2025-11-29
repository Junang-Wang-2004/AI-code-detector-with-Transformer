v1 = int(input())
v2 = ['' for v3 in range(v1)]
for v3 in range(v1):
    for v4 in range(v1):
        if v4 < v3:
            v2[v4] += alf[v4]
        else:
            v2[v4] += alf[v3]
print(*v2, sep='\n')
