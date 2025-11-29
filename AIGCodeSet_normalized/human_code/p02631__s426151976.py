import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10 ** 9))
v1 = lambda x: sys.stdout.write(x + '\n')
v2 = int(input())
v3 = list(map(int, input().split()))
v4 = 0
for v5 in v3:
    v4 = v4 ^ v5
v6 = [None] * v2
for v7, v5 in enumerate(v3):
    v6[v7] = v4 ^ v5
v1(' '.join(map(str, v6)))
