import collections

class C1(object):

    def countTheNumOfKFreeSubsets(self, a1, a2):
        v1 = collections.Counter(a1)
        v2 = set(v1)
        v3 = sorted(v1)
        v4 = 1
        for v5 in v3:
            if v5 - a2 in v2:
                continue
            v6 = 1
            v7 = 0
            v8 = v5
            while v8 in v1:
                v9 = v1[v8]
                v10 = 2 ** v9 - 1
                v11 = v6 + v7
                v12 = v6 * v10
                v6 = v11
                v7 = v12
                v8 += a2
            v13 = v6 + v7
            v4 *= v13
        return v4
