class C1(object):

    def closetTarget(self, a1, a2, a3):
        """
        """
        v1 = float('inf')
        v2 = v1
        for v3, v4 in enumerate(a1):
            if v4 == a2:
                v2 = min(v2, (v3 - a3) % len(a1), (a3 - v3) % len(a1))
        return v2 if v2 != v1 else -1
