class C1(object):

    def maxProduct(self, a1):
        """
        """

        def counting_sort(a1):
            v1 = 1000
            v2 = [[] for v3 in range(v1)]
            for v4 in a1:
                v2[len(v4)].append(v4)
            v5 = []
            for v6 in reversed(range(v1)):
                if v2[v6]:
                    v5 += v2[v6]
            return v5
        a1 = counting_sort(a1)
        v2 = [0] * len(a1)
        for v3, v4 in enumerate(a1):
            for v5 in v4:
                v2[v3] |= 1 << ord(v5) - ord('a')
        v6 = 0
        for v3 in range(len(a1) - 1):
            if len(a1[v3]) ** 2 <= v6:
                break
            for v7 in range(v3 + 1, len(a1)):
                if len(a1[v3]) * len(a1[v7]) <= v6:
                    break
                if not v2[v3] & v2[v7]:
                    v6 = len(a1[v3]) * len(a1[v7])
        return v6
