import sys
from typing import Any, Callable, Deque, Dict, List, Mapping, Optional, Sequence, Set, Tuple, TypeVar, Union

def f1():
    v1 = Union[int, float]
    v2 = 1000000007
    v3 = float('inf')
    sys.setrecursionlimit(10 ** 6)

    def input():
        return sys.stdin.readline().rstrip()

    def ii():
        return int(input())

    def isp():
        return input().split()

    def mi():
        return map(int, input().split())

    def mi_0():
        return map(lambda x: int(x) - 1, input().split())

    def lmi():
        return list(map(int, input().split()))

    def lmi_0():
        return list(map(lambda x: int(x) - 1, input().split()))

    def li():
        return list(input())
    v4 = ii()
    v5, v6, v7 = (0, 0, 0)
    v8 = 0
    for v9 in range(v4):
        v10 = input()
        v8 += v10.count('AB')
        if v10[0] == 'B' and v10[-1] == 'A':
            v5 += 1
        elif v10[0] == 'B':
            v6 += 1
        elif v10[-1] == 'A':
            v7 += 1
    if v6 and v7:
        if v5:
            v8 += v5 + 1
            v6 -= 1
            v7 -= 1
        v8 += min(v6, v7)
    elif v6 or v7:
        v8 += v5
    else:
        v8 += max(v5 - 1, 0)
    print(v8)
if __name__ == '__main__':
    f1()
