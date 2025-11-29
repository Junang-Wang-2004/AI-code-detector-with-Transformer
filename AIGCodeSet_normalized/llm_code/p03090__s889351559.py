import sys

def f1():
    return sys.stdin.readline()[:-1]
v1 = float('inf')
v2 = int(f1())
v3 = (v2 + 1) // 2 * (v2 - 2)
if v2 % 2 == 0:
    print(v2 * (v2 - 2) // 2)
else:
    print((v2 - 1) * (v2 - 3) // 2 + v2 - 1)
for v4 in range(v2):
    for v5 in range(v4 + 1, v2):
        if v4 + 1 + (v5 + 1) != v2 + (v2 + 1) % 2:
            print(v4 + 1, v5 + 1)
