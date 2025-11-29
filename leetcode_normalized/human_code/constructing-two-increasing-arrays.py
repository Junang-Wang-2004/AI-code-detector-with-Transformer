class C1(object):

    def minLargest(self, a1, a2):
        """
        """
        if len(a1) < len(a2):
            a1, a2 = (a2, a1)
        v3 = [float('inf')] * (len(a2) + 1)
        v3[0] = 0
        for v4 in range(len(a1) + 1):
            for v5 in range(len(a2) + 1):
                if not v4 and (not v5):
                    continue
                v6 = float('inf')
                if v4 - 1 >= 0:
                    v6 = min(v6, v3[v5] + (2 if v3[v5] % 2 == a1[v4 - 1] % 2 else 1))
                if v5 - 1 >= 0:
                    v6 = min(v6, v3[v5 - 1] + (2 if v3[v5 - 1] % 2 == a2[v5 - 1] % 2 else 1))
                v3[v5] = v6
        return v3[-1]
