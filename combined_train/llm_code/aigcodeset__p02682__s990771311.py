import sys

def f1():
    return list(map(int, sys.stdin.readline().split()))
v1 = f1()
v2 = 0
if v1[3] >= v1[0]:
    v1[3] -= v1[0]
    v2 = v1[0]
    if v1[3] <= v1[1]:
        pass
        v1[3] -= v1[1]
        v2 -= v1[3]
    else:
        v1[3] -= v1[1]
        v2 -= v1[3]
elif v1[3] <= v1[0]:
    v2 = v1[3]
else:
    v2 = v1[0]
print(v2)
