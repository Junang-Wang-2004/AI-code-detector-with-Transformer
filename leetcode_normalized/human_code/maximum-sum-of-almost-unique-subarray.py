import collections

class C1(object):

    def maxSum(self, a1, a2, a3):
        """
        """
        v1 = collections.Counter()
        v2 = v3 = v4 = 0
        for v5 in range(len(a1)):
            v3 += a1[v5]
            v1[a1[v5]] += 1
            if v5 - v4 + 1 == a3 + 1:
                v1[a1[v4]] -= 1
                if v1[a1[v4]] == 0:
                    del v1[a1[v4]]
                v3 -= a1[v4]
                v4 += 1
            if v5 - v4 + 1 == a3 and len(v1) >= a2:
                v2 = max(v2, v3)
        return v2
