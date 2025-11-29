"""
D - Blue and Red Balls
https://atcoder.jp/contests/abc132/tasks/abc132_d

"""
import sys
v1 = [1]
for v2 in range(1, 2001):
    v1.append(v1[-1] * v2)

def f1(a1, a2):
    v1 = 10 ** 9 + 7
    v2 = []
    for v3 in range(1, a2 + 1):
        v4 = v1[a2 - 1] // (v1[v3 - 1] * v1[a2 - 1 - v3 + 1])
        v5 = v1[a1 - a2 + 1] // (v1[v3] * v1[a1 - a2 + 1 - v3])
        v2.append(v4 * v5 % v1)
    return v2

def f2(a1):
    v1, v2 = map(int, input().split())
    v3 = f1(v1, v2)
    print(*v3, sep='\n')
if __name__ == '__main__':
    f2(sys.argv[1:])
