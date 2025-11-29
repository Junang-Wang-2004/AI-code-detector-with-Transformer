"""
AtCoder :: Beginner Contest 174 :: Logs
https://atcoder.jp/contests/abc174/tasks/abc174_e
"""
import sys
from math import ceil

def f1():
    """Main program."""
    v1, v2 = (int(i) for v3 in sys.stdin.readline().split())
    v4 = [int(v3) for v3 in sys.stdin.readline().split()]
    v5 = max(v4)
    v6 = 1
    v7 = v5
    while v6 <= v5:
        v8 = (v6 + v5) // 2
        v9 = sum([int(ceil(log / v8)) - 1 for v10 in v4])
        if v9 <= v2:
            v7 = min(v7, v8)
            v5 = v8 - 1
        else:
            v6 = v8 + 1
    print(v7)
if __name__ == '__main__':
    f1()
