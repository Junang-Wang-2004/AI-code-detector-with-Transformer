import sys
from typing import List

def f1() -> tuple:
    return map(int, sys.stdin.readline().split())

def f2(a1: List[int], a2: int, a3: int) -> bool:
    v1 = 0
    for v2 in a1:
        v1 += (v2 - 1) // a3
    return v1 <= a2

def f3(a1: List[int], a2: int) -> int:
    v1, v2 = (1, max(a1))
    while v1 < v2:
        v3 = (v1 + v2) // 2
        if f2(a1, a2, v3):
            v2 = v3
        else:
            v1 = v3 + 1
    return v1

def f4() -> None:
    v1, v2 = f1()
    v3 = list(f1())
    v4 = f3(v3, v2)
    print(v4)
if __name__ == '__main__':
    f4()
