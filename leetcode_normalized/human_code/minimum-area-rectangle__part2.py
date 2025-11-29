class C1(object):

    def minAreaRect(self, a1):
        """
        """
        v1 = set()
        v2 = float('inf')
        for v3, v4 in a1:
            for v5, v6 in v1:
                if (v3, v6) in v1 and (v5, v4) in v1:
                    v2 = min(v2, abs(v3 - v5) * abs(v4 - v6))
            v1.add((v3, v4))
        return v2 if v2 != float('inf') else 0
