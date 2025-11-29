def f1(a1):
    return a1 * (a1 + 1) // 2
from sys import exit
v1, v2 = [int(n) for v3 in input().split()]
if f1(v1 - 2) < v2:
    print(-1)
    exit()
for v4 in range(2, v1 + 1):
    print(1, v4)
v5 = f1(v1 - 2) - v2
while v5 != 0:
    for v4 in range(2, v1):
        for v6 in range(v4 + 1, v1 + 1):
            print(v4, v6)
            v5 -= 1
            if v5 == 0:
                exit()
