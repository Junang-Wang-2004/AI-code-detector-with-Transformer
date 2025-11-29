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
    return v2
v1 = 10 ** 6
v2 = f1(v1)

class C1(object):

    def minJumps(self, a1):
        """
        """
        v1 = collections.defaultdict(list)
        for v2, v3 in enumerate(a1):
            while v3 != 1:
                v4 = v2[v3]
                while v3 % v4 == 0:
                    v3 //= v4
                v1[v4].append(v2)
        v5 = [-1] * len(a1)
        v5[0] = 0
        v6 = [0]
        while v6:
            v7 = []
            for v2 in v6:
                if v2 == len(a1) - 1:
                    return v5[-1]
                for v8 in (-1, +1):
                    v9 = v2 + v8
                    if 0 <= v9 < len(a1) and v5[v9] == -1:
                        v5[v9] = v5[v2] + 1
                        v7.append(v9)
                v4 = a1[v2]
                if v2[v4] != v4 or v4 not in v1:
                    continue
                for v9 in v1[v4]:
                    if v5[v9] != -1:
                        continue
                    v5[v9] = v5[v2] + 1
                    v7.append(v9)
                del v1[v4]
            v6 = v7
        return -1
