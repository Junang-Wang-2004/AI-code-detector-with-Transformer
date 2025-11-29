import heapq
v1, v2 = map(int, input().split())

def f1(a1):
    if a1 % v1 == 0:
        return v1
    else:
        return a1 % v1
if v1 % 2 == 1:
    for v3 in range(v2):
        print(v3 + 1, v1 - v3)
else:
    v4 = set()
    for v5 in range(1, v2 + 1):
        for v6 in range(v1):
            v7 = f1(v6 + v5)
            if v6 in v4 or v7 in v4:
                continue
            else:
                print(v6 + 1, v7 + 1)
                v4.add(v6)
                v4.add(v7)
                break
