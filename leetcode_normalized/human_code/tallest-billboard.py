import collections

class C1(object):

    def tallestBillboard(self, a1):
        """
        """

        def dp(a1):
            v1 = collections.defaultdict(int)
            v1[0] = 0
            for v2 in a1:
                for v3, v4 in list(v1.items()):
                    v1[v3 + v2] = max(v1[v3 + v2], v4)
                    v1[abs(v3 - v2)] = max(v1[abs(v3 - v2)], v4 + min(v3, v2))
            return v1
        v1, v2 = (dp(a1[:len(a1) // 2]), dp(a1[len(a1) // 2:]))
        return max((v1[d] + v2[d] + d for v3 in v1 if v3 in v2))
