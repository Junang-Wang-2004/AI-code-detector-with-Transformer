class C1(object):

    def closestToTarget(self, a1, a2):
        """
        """
        v1, v2 = (float('inf'), set())
        for v3 in a1:
            v2 = {v3} | {f & v3 for v4 in v2}
            for v4 in v2:
                v1 = min(v1, abs(v4 - a2))
        return v1
