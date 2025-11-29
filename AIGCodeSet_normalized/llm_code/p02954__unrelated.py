from collections import deque

def f1(a1):
    v1 = len(a1)
    v2 = [1] * v1
    v3 = [1 if c == 'R' else -1 for v4 in a1]
    for v5 in range(1, v1 - 1):
        if v3[v5] == 1:
            v2[v5 + 1] += v2[v5]
            v2[v5] = 0
        else:
            v2[v5 - 1] += v2[v5]
            v2[v5] = 0
    return v2
v1 = input()
v2 = f1(v1)
print(*v2)
