import sys
v1 = int(sys.stdin.readline())
v2 = [['a']]
v3 = ('a', 'b')
for v4 in range(v1 - 1):
    v5 = []
    for v6 in v2[-1]:
        for v7 in v3:
            if v7 >= v6[-1]:
                v5.append(v6 + v7)
    v2.append(v5)
v2[-1].sort()
print('\n'.join(v2[-1]))
