import sys
from collections import defaultdict

def f1():
    v1, v2 = map(int, sys.stdin.readline().split())
    v3 = []
    for v4 in range(v2):
        v5, v6 = map(int, sys.stdin.readline().split())
        v7 = list(map(int, sys.stdin.readline().split()))
        v3.append((v5, v6, v7))
    v8 = defaultdict(list)
    for v5, v6, v7 in v3:
        for v9 in v7:
            v8[v9].append((v5, v6, v7))
    v10 = float('inf')

    def backtrack(a1, a2, a3):
        nonlocal min_cost
        if a1 == v1 + 1:
            v1 = min(v1, a3)
            return
        if a3 >= v1:
            return
        for v2 in v8[a1]:
            v3, v4, v5 = v2
            if v2 not in a2:
                a2.append(v2)
                for v6 in range(a1 + 1, a1 + v4 + 1):
                    backtrack(v6, a2, a3 + v3)
                a2.pop()
    backtrack(1, [], 0)
    if v10 != float('inf'):
        print(v10)
    else:
        print(-1)
if __name__ == '__main__':
    f1()
