import sys
input = sys.stdin.readline
v1, v2, v3, v4, v5 = map(int, input().split())
v6 = v1 * 60 + v2
v7 = v3 * 60 + v4
if v7 - v6 >= v5:
    print(v7 - v6 - v5)
else:
    print(0)
