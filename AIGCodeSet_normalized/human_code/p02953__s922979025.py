import sys
v1 = int(input())
v2 = list(map(int, input().split()))
v3 = -float('inf')
for v4 in v2:
    if v4 < v3:
        if v4 + 1 != v3:
            print('No')
            sys.exit()
        else:
            v3 = v4 + 1
    else:
        v3 = v4
print('Yes')
