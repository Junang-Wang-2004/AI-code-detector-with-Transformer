import sys

def f1():
    v1 = int(input())
    v2 = 0
    for v3 in range(1, v1, 2):
        if f2(v3):
            v2 += 1
    print(v2)

def f2(a1):
    v1 = 2
    v2 = a1
    v3 = 3
    while True:
        if v2 <= v3:
            break
        if a1 % v3 == 0:
            v1 += 2
            v2 = a1 // v3
        v3 += 2
    return True if v1 == 8 else False
if '__main__' == __name__:
    f1()
