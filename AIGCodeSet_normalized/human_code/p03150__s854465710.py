v1 = list(input())
v2 = len(v1)
v3 = 'NO'
for v4 in range(v2):
    for v5 in range(1, v2):
        v6 = v1.copy()
        del v6[v4:v5]
        if v6 == ['k', 'e', 'y', 'e', 'n', 'c', 'e']:
            v3 = 'YES'
            break
print(v3)
