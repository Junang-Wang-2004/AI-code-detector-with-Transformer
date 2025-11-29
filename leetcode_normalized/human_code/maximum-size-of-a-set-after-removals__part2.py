class C1(object):

    def maximumSetSize(self, a1, a2):
        """
        """
        v1, v2 = (set(a1), set(a2))
        v3, v4 = (len(a1), len(v1 & v2))
        v5, v6 = (min(len(v1) - v4, v3 // 2), min(len(v2) - v4, v3 // 2))
        v7, v8 = (v3 // 2 - v5, v3 // 2 - v6)
        return v5 + v6 + min(v7 + v8, v4)
