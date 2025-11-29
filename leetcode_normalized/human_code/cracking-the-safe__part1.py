class C1(object):

    def crackSafe(self, a1, a2):
        """
        """
        v1 = a2 ** (a1 - 1)
        v2 = [q * a2 + i for v3 in range(a2) for v4 in range(v1)]
        v5 = [str(a2 - 1)] * (a1 - 1)
        for v3 in range(a2 ** a1):
            v6 = v3
            while v2[v6] >= 0:
                v5.append(str(v6 // v1))
                v2[v6], v6 = (-1, v2[v6])
        return ''.join(v5)
