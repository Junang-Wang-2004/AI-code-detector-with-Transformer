import sys
import math

def f1(a1):
    return int(a1)

def f2(a1):
    v1 = f1(a1[1])
    print(v1 ** 2)
if __name__ == '__main__':
    f2(sys.argv)
