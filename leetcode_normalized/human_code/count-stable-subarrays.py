class C1(object):

    def countStableSubarrays(self, a1, a2):
        """
        """

        def count(a1):
            return (a1 + 1) * a1 // 2
        v1 = list(range(len(a1)))
        for v2 in reversed(range(len(a1) - 1)):
            if a1[v2] <= a1[v2 + 1]:
                v1[v2] = v1[v2 + 1]
        v3 = [0] * (len(a1) + 1)
        v4 = 0
        for v2 in range(len(a1)):
            if v2 - 1 >= 0 and a1[v2 - 1] > a1[v2]:
                v4 = 0
            v4 += 1
            v3[v2 + 1] = v3[v2] + v4
        return [count(min(v1[l], r) - l + 1) + (v3[r + 1] - v3[min(v1[l], r) + 1]) for v5, v6 in a2]
