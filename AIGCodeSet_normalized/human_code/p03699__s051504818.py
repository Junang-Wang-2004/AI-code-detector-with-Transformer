v1 = int(input())
v2 = []
v3 = 0
for v4 in range(v1):
    v5 = int(input())
    v2 += [v5]
    v3 += v5
v2.sort()
if v3 % 10 != 0:
    print(v3)
    exit()
else:
    for v6 in range(v1):
        if v2[v6] % 10 != 0:
            print(v3 - v2[v6])
            exit()
print(0)
