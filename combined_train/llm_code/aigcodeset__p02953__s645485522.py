import sys
v1 = int(input())
v2 = list(map(int, input().split()))
if len(v2) < 1:
    print('Yes')
    sys.exit()
v3 = False
v4 = v2[0]
v5 = 0
for v6 in range(len(v2) - 1):
    if v2[v6] > v2[v6 + 1]:
        v2[v6] -= 1
        if v2[v6] > v4:
            v4 = v2[v6]
        if v2[v6] < v4:
            print('No')
            sys.exit()
if v2[-1] < v2[-2]:
    print('No')
    sys.exit()
if not v3:
    print('Yes')
