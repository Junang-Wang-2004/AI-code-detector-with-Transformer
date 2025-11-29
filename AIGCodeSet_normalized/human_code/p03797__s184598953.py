import sys
v1, v2 = map(int, sys.stdin.readline().split())

def f1():
    if v1 >= v2 // 2:
        v1 = v2 // 2
    else:
        v1 = v1 + (v2 - 2 * v1) // 4
    print(v1)
if __name__ == '__main__':
    f1()
