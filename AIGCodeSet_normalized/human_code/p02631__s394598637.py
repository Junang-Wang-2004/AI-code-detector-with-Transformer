import sys
v1 = 1 << 60
v2 = 10 ** 9 + 7
sys.setrecursionlimit(2147483647)
input = lambda: sys.stdin.readline().rstrip()

def f1():
    v1 = int(input())
    v2 = list(map(int, input().split()))
    v3 = 0
    for v4 in v2:
        v3 ^= v4
    v5 = [v4 ^ v3 for v4 in v2]
    print(*v5)
f1()
