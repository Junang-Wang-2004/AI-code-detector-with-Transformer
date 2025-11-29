import sys

def f1(a1, a2, a3):
    v1 = a2
    v2 = a3
    v3 = v1 + v2
    if v3 > a1:
        return 0
    else:
        return a1 - v3
if __name__ == '__main__':
    v1 = int(input())
    v2 = int(input())
    v3 = int(input())
    print(f1(v1, v2, v3))
