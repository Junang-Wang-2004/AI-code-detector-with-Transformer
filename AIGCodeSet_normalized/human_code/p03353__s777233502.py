import sys
v1 = input()
v2 = int(input())
v3 = sorted(set(v1))
v4 = []
for v5 in v3:
    v6 = v5
    while v6 in v1:
        v4.append(v6)
        if len(v4) == v2:
            print(v4[v2 - 1])
            sys.exit()
        for v7 in range(len(v3)):
            if v6 + v3[v7] in v1:
                v6 = v6 + v3[v7]
                break
        else:
            break
print(v4[v2 - 1])
