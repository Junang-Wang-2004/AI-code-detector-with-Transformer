import bisect

class C1(object):

    def makeArrayIncreasing(self, a1, a2):
        v1 = sorted(set(a2))
        v2 = len(a1)
        v3 = 10 ** 18 + 42
        v4 = [-1] + [v3] * v2
        for v5 in a1:
            v6 = [v3] * (v2 + 1)
            for v7 in range(v2 + 1):
                v8 = v4[v7]
                if v8 == v3:
                    continue
                if v8 < v5:
                    v6[v7] = min(v6[v7], v5)
                v9 = bisect.bisect_right(v1, v8)
                if v9 < len(v1):
                    v10 = v7 + 1
                    if v10 <= v2:
                        v6[v10] = min(v6[v10], v1[v9])
            if all((e == v3 for v11 in v6)):
                return -1
            v4 = v6
        for v7 in range(v2 + 1):
            if v4[v7] != v3:
                return v7
        return -1
