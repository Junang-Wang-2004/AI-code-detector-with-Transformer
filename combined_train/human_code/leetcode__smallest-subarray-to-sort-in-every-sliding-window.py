class C1(object):

    def minSubarraySort(self, a1, a2):
        """
        """

        def count(a1):
            v1, v2 = ([n] * n, [])
            for v3 in reversed(range(n)):
                while not (not v2 or a1[v2[-1]] >= a1[v3]):
                    v2.pop()
                if v2:
                    v1[v3] = v2[-1]
                v2.append(v3)
            v4 = []
            v5, v6 = (0, -1)
            for v3 in range(1, n):
                if a1[v3] < a1[v3 - 1]:
                    v6 = v3
                if v3 < a2 - 1:
                    continue
                v5 = max(v5, v3 - (a2 - 1))
                while not v1[v5] > v6:
                    v5 = v1[v5]
                v4.append(max(v3 - v1[v5] + 1, 0))
            return v4
        v1 = len(a1)
        if a2 == 1:
            return [0] * (v1 - a2 + 1)
        v2 = count(a1)
        for v3 in range((v1 + 1) // 2):
            a1[v3], a1[~v3] = (-a1[~v3], -a1[v3])
        v4 = count(a1)
        return [max(a2 - v4[~v3] - v2[v3], 0) for v3 in range(v1 - a2 + 1)]
