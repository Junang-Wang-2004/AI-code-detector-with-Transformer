class C1(object):

    def vowelStrings(self, a1, a2):
        """
        """
        v1 = {'a', 'e', 'i', 'o', 'u'}
        v2 = [0] * (len(a1) + 1)
        for v3, v4 in enumerate(a1):
            v2[v3 + 1] = v2[v3] + int(v4[0] in v1 and v4[-1] in v1)
        return [v2[r + 1] - v2[l] for v5, v6 in a2]
