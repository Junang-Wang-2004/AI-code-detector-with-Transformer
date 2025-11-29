class C1(object):

    def countLatticePoints(self, a1):
        """
        """
        v1 = set()
        for v2, v3, v4 in a1:
            for v5 in range(-v4, v4 + 1):
                for v6 in range(-v4, v4 + 1):
                    if v5 ** 2 + v6 ** 2 <= v4 ** 2:
                        v1.add((v2 + v5, v3 + v6))
        return len(v1)
