import sys
input = sys.stdin.readline
v1, v2 = map(int, input().split())
if v1 % v2 == 0:
    print(-1)
else:
    print(v1)
