class C1(object):

    def assignElements(self, a1, a2):
        """
        """
        v1 = max(a1)
        v2 = [-1] * v1
        for v3, v4 in enumerate(a2):
            if v4 > v1 or v2[v4 - 1] != -1:
                continue
            for v5 in range(v4, v1 + 1, v4):
                if v2[v5 - 1] == -1:
                    v2[v5 - 1] = v3
        return [v2[v4 - 1] for v4 in a1]
