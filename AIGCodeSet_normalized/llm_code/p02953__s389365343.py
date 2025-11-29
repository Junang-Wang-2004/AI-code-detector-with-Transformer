import sys
v1 = int(input())
v2 = list(map(int, input().split()))
if len(v2) == 1:
    print('Yes')
    sys.exit()
for v3 in range(1, v1)[::-1]:
    if v2[v3] >= v2[v3 - 1]:
        v2[v3 - 1] -= 1
    elif v2[v3] < v2[v3 - 1] and v2[v3] >= v2[v3 - 1] - 1:
        continue
    else:
        print('No')
        sys.exit()
print('Yes')
