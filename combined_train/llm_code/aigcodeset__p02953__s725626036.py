v1 = int(input())
v2 = list(map(int, input().split()))
v3 = []
import sys
for v4 in range(v1 - 1):
    v3.append(v2[v4 + 1] - v2[v4])
if any((v4 <= -2 for v4 in v3)):
    print('No')
    sys.exit()
for v4 in range(v1 - 1):
    v5 = v3[v4]
    for v6 in range(v4 + 1, v1 - 1):
        if v5 < 0:
            v5 += v3[v6]
            if v6 == v1 - 2:
                print('No')
                sys.exit()
        else:
            break
print('Yes')
