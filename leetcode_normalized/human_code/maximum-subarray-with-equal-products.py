import collections

def f1(a1):
    v1 = []
    v2 = [-1] * (a1 + 1)
    for v3 in range(2, a1 + 1):
        if v2[v3] == -1:
            v2[v3] = v3
            v1.append(v3)
        for v4 in v1:
            if v3 * v4 > a1 or v4 > v2[v3]:
                break
            v2[v3 * v4] = v4
    return v1

def f2(a1):
    v1 = [[] for v2 in range(a1 + 1)]
    for v3 in f1(a1):
        for v4 in range(v3, a1 + 1, v3):
            v1[v4].append(v3)
    return v1
v1 = 10
v2 = f2(v1)

class C1(object):

    def maxLength(self, a1):
        """
        """
        v1 = 2
        v2 = collections.defaultdict(int)
        v3 = 0
        for v4, v5 in enumerate(a1):
            for v6 in v2[v5]:
                v3 = max(v3, v2[v6])
                v2[v6] = v4 + 1
            v1 = max(v1, v4 - v3 + 1)
        return v1
