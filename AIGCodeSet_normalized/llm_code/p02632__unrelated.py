import sys
v1 = 10 ** 9 + 7

def f1():
    v1 = int(sys.stdin.readline())
    v2 = sys.stdin.readline().strip()
    v3 = len(v2)
    v4 = 1
    for v5 in range(v1):
        v4 = v4 * (v3 + v5 + 1) % v1
    print(v4)
if __name__ == '__main__':
    f1()
