class C1(object):

    def simulationResult(self, a1, a2):
        """
        """
        v1 = [False] * len(a1)
        v2 = []
        for v3 in reversed(a2):
            if v1[v3 - 1]:
                continue
            v1[v3 - 1] = True
            v2.append(v3)
        v2.extend((v3 for v3 in a1 if not v1[v3 - 1]))
        return v2
