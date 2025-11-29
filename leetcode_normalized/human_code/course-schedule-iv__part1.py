class C1(object):

    def checkIfPrerequisite(self, a1, a2, a3):
        """
        """

        def floydWarshall(a1, a2):
            v1 = set([x[0] * a1 + x[1] for v2 in a2])
            for v3 in range(a1):
                for v4 in range(a1):
                    for v5 in range(a1):
                        if v4 * a1 + v5 not in v1 and (v4 * a1 + v3 in v1 and v3 * a1 + v5 in v1):
                            v1.add(v4 * a1 + v5)
            return v1
        v1 = floydWarshall(a1, a2)
        return [i * a1 + j in v1 for v2, v3 in a3]
