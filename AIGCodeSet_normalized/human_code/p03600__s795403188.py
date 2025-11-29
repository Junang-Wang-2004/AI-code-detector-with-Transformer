import sys
from itertools import permutations, combinations

def f1():
    input = sys.stdin.readline
    v1 = int(input())
    v2 = [[int(a) for v3 in input().split()] for v4 in range(v1)]
    v5 = 0
    v6 = True
    for v3 in range(v1):
        for v7, v8 in enumerate(v2[v3]):
            for v9 in range(v1):
                if v9 != v3 and v9 != v7:
                    if v8 > v2[v3][v9] + v2[v9][v7]:
                        v6 = False
                        break
                    elif v8 == v2[v3][v9] + v2[v9][v7]:
                        break
            else:
                v5 += v8
        if not v6:
            print(-1)
            break
    else:
        print(v5 // 2)
    return 0
if __name__ == '__main__':
    f1()
