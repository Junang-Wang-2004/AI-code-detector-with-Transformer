class C1(object):

    def stringMatching(self, a1):
        """
        """
        v1 = []
        for v2, v3 in enumerate(a1):
            for v4, v5 in enumerate(a1):
                if v2 != v4 and v3 in v5:
                    v1.append(v3)
                    break
        return v1
