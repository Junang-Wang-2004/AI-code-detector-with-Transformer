import sys

def f1():
    v1, v2 = map(int, input().split())
    v3 = 1
    v4 = v2
    while v1 >= v4:
        v4 *= v2
        v3 += 1
    print(v3)
if __name__ == '__main__':
    f1()
