class C1(object):

    def circularGameLosers(self, a1, a2):
        """
        """
        v1 = [False] * a1
        v2 = 0
        for v3 in range(a1):
            if v1[v2]:
                break
            v1[v2] = True
            v2 = (v2 + (v3 + 1) * a2) % a1
        return [v3 + 1 for v3 in range(a1) if not v1[v3]]
