import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
v1 = float('inf')
v2 = 10 ** 9 + 7

def f1():
    v1 = int(input())
    v2 = []
    v3 = v1
    if v1 % 2 != 0:
        v3 -= 1
    for v4 in range(1, v1 + 1):
        for v5 in range(v4 + 1, v1 + 1):
            if v5 == v3:
                continue
            v2.append([v4, v5])
        v3 -= 1
    print(len(v2))
    for v4 in v2:
        print(*v4)
if __name__ == '__main__':
    f1()
