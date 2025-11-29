"""
https://atcoder.jp/contests/tokiomarine2020/submissions/14229099
"""
v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))

def f1(a1):
    v1 = [0] * v1
    for v2, v3 in enumerate(a1):
        v4 = max(0, v2 - v3)
        v5 = min(v1 - 1, v2 + v3)
        v1[v4] += 1
        if v5 + 1 < v1:
            v1[v5 + 1] -= 1
    v6 = []
    v7 = 0
    for v2 in v1:
        v7 += v2
        v6.append(v7)
    return v6
for v4 in range(min(v2, 75)):
    v3 = f1(v3)
print(*v3)
