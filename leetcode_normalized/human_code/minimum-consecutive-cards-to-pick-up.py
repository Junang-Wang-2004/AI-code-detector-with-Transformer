class C1(object):

    def minimumCardPickup(self, a1):
        """
        """
        v1 = {}
        v2 = float('inf')
        for v3, v4 in enumerate(a1):
            if v4 in v1:
                v2 = min(v2, v3 - v1[v4] + 1)
            v1[v4] = v3
        return v2 if v2 != float('inf') else -1
