from collections import defaultdict

def f1(a1):
    v1 = len(a1)
    v2 = [0] * (v1 + 1)
    v3 = [1] * (v1 + 1)
    v4 = 10 ** 9 + 7
    v5 = 257
    for v6 in range(v1):
        v2[v6 + 1] = (v2[v6] + (ord(a1[v6]) - ord('a') + 1) * v3[v6]) % v4
        v3[v6 + 1] = v3[v6] * v5 % v4
    v7 = set()
    for v6 in range(v1):
        for v8 in range(v6, v1):
            v9 = (v2[v8 + 1] - v2[v6] + v4) % v4
            v7.add(v9)
    return len(v7)
v1 = input()
v2 = f1(v1)
print(v2)
