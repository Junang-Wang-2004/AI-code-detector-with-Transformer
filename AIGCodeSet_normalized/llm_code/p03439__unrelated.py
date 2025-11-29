import sys

def f1(a1):
    v1 = [None] * a1
    for v2 in range(a1):
        if v1[v2] == 'Vacant':
            return v2
        print(v2)
        sys.stdout.flush()
        v3 = input()
        v1[v2] = v3
    return -1
v1 = int(input())
v2 = f1(v1)
print(v2)
