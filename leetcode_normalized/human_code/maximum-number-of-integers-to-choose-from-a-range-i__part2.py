import bisect

class C1(object):

    def maxCount(self, a1, a2, a3):
        """
        """

        def check(a1):
            return (a1 + 1) * a1 // 2 - prefix[bisect.bisect_right(sorted_banned, a1)] <= a3
        v1 = sorted(set(a1))
        v2 = [0] * (len(v1) + 1)
        for v3 in range(len(v1)):
            v2[v3 + 1] = v2[v3] + v1[v3]
        v4, v5 = (1, a2)
        while v4 <= v5:
            v6 = v4 + (v5 - v4) // 2
            if not check(v6):
                v5 = v6 - 1
            else:
                v4 = v6 + 1
        return v5 - bisect.bisect_right(v1, v5)
