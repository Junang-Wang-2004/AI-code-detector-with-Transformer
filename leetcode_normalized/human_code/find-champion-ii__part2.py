class C1(object):

    def findChampion(self, a1, a2):
        """
        """
        v1 = {v for v2, v3 in a2}
        return next((u for v4 in range(a1) if v4 not in v1)) if len(v1) == a1 - 1 else -1
