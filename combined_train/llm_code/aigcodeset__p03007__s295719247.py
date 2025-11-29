import sys

def f1():
    return sys.stdin.readline().rstrip()
from collections import deque

def f2():
    v1 = int(f1())
    v2 = list(map(int, f1().split()))
    v2.sort(reverse=True)
    v3 = deque(v2)
    v4 = deque()
    while len(v3) >= 2:
        if v3[-1] >= 0:
            break
        v4.append(v3.pop())
    if not v4:
        v4.append(v3.pop())
    v5 = []
    while len(v3) >= 2:
        v6 = v3.pop()
        v7 = v4.pop()
        v5.append((v7, v6))
        v4.append(v7 - v6)
    v8 = v3.pop()
    while len(v4) >= 2:
        v7 = v4.popleft()
        v5.append((v7, v8))
        v8 += -v7
    v9 = v4.pop()
    v5.append((v8, v9))
    print(v8 - v9)
    for v6, v7 in v5:
        print(v6, v7)
if __name__ == '__main__':
    f2()
