import sys
v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 10 ** 18
if 0 in v2:
    print(0)
    sys.exit()
v4 = 1
for v5 in v2:
    v4 *= v5
    if v4 > v3:
        print(-1)
        sys.exit()
print(v4)
