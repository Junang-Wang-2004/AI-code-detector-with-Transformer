class C1(object):

    def rankTeams(self, a1):
        """
        """
        v1 = {v: [0] * len(a1[0]) + [v] for v2 in a1[0]}
        for v3 in a1:
            for v4, v2 in enumerate(v3):
                v1[v2][v4] -= 1
        return ''.join(sorted(a1[0], key=v1.__getitem__))
