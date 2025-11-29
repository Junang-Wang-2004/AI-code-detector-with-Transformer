class C1(object):

    def findOriginalArray(self, a1):
        """
        """
        if len(a1) % 2:
            return []
        v1 = collections.Counter(a1)
        for v2 in sorted(v1.keys()):
            if v1[v2] > v1[2 * v2]:
                return []
            v1[2 * v2] -= v1[v2] if v2 else v1[v2] // 2
        return list(v1.elements())
