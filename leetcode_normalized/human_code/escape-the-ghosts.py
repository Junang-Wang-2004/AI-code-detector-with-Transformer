class C1(object):

    def escapeGhosts(self, a1, a2):
        """
        """
        v1 = abs(a2[0]) + abs(a2[1])
        return all((v1 < abs(a2[0] - i) + abs(a2[1] - j) for v2, v3 in a1))
