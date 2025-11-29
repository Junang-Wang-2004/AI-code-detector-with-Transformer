import collections

class C1(object):

    def maxOperations(self, a1, a2):
        v1 = collections.Counter(a1)
        v2 = 0
        for v3 in v1:
            v4 = a2 - v3
            if v4 < v3:
                continue
            if v4 == v3:
                v2 += v1[v3] // 2
            else:
                v2 += min(v1[v3], v1[v4])
        return v2
