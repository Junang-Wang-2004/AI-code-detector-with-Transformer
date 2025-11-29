class C1(object):

    def maxProduct(self, a1):
        """
        """
        a1.sort(key=lambda x: len(x), reverse=True)
        v1 = [0] * len(a1)
        for v2, v3 in enumerate(a1):
            for v4 in v3:
                v1[v2] |= 1 << ord(v4) - ord('a')
        v5 = 0
        for v2 in range(len(a1) - 1):
            if len(a1[v2]) ** 2 <= v5:
                break
            for v6 in range(v2 + 1, len(a1)):
                if len(a1[v2]) * len(a1[v6]) <= v5:
                    break
                if not v1[v2] & v1[v6]:
                    v5 = len(a1[v2]) * len(a1[v6])
        return v5
