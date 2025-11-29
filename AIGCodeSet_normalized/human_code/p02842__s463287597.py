import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
v1 = 10 ** 30

def f1():
    v1 = int(input().strip())
    for v2 in range(50000):
        if int(v2 * 1.08) == v1:
            print(v2)
            return 0
    print(':(')
if __name__ == '__main__':
    f1()
