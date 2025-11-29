from sys import stdin
v1 = int(stdin.readline().rstrip())
v2 = stdin.readline().rstrip()
v3 = 0
v4 = [str(i).zfill(3) for v5 in range(1000)]
for v5 in v4:
    v6 = 0
    v7 = 0
    while v7 < 3:
        while v6 < len(v2):
            if v2[v6] == v5[v7]:
                v7 += 1
                v6 += 1
                break
            v6 += 1
        if v6 == len(v2):
            break
    if v7 == 3:
        v3 += 1
print(v3)
