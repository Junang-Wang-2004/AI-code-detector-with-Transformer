import sys
input = sys.stdin.readline
v1, v2 = map(int, input().split())
v3, v4 = map(int, input().split())
v5, v6 = map(int, input().split())
v7 = (v1 * v3, v2 * v4)
v8 = (v1 * v5, v2 * v6)
if sum(v7) == sum(v8):
    print('infinity')
    sys.exit()
if v7[0] > v8[0]:
    v7, v8 = (v8, v7)
if sum(v7) < sum(v8):
    print(0)
    sys.exit()
v9 = (v8[0] - v7[0]) // (sum(v7) - sum(v8))
v10 = 0
if (v8[0] - v7[0]) % (sum(v7) - sum(v8)) == 0:
    v10 = 1
print(v9 * 2 + 1 - v10)
