import collections

class C1(object):

    def maxRepOpt1(self, a1):
        v1 = collections.Counter(a1)
        v2 = 0
        v3 = len(a1)
        for v4 in v1:
            v5 = 0
            v6 = 0
            for v7 in range(v3):
                if a1[v7] != v4:
                    v5 += 1
                while v5 > 1 and v6 <= v7:
                    if a1[v6] != v4:
                        v5 -= 1
                    v6 += 1
                v8 = v7 - v6 + 1
                v2 = max(v2, min(v8, v1[v4]))
        return v2
