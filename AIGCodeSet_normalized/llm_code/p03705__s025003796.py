import sys
v1, v2, v3 = map(int, input().split())
if v1 == 1:
    if v2 != v3:
        print(0)
    else:
        print(1)
    sys.exit()
if v1 == 2:
    if v2 > v3:
        print(0)
    else:
        print(1)
    sys.exit()
if v2 > v3:
    print(0)
    sys.exit()
if v2 > 1000000007 and v3 > 1000000007:
    v2 = v2 % 1000000007
    v3 = v3 % 1000000007
v4 = v2 * v1
v5 = v3 * v1
if v4 > v5:
    print(0)
else:
    print(v5 - v4 + 1)
