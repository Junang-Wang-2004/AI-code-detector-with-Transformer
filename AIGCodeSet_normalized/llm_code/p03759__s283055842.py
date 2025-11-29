import sys
input = sys.stdin.readline
v1, v2, v3 = map(int, input().split())
if v2 - v1 == v3 - v2:
    print('YES')
else:
    print('NO')
