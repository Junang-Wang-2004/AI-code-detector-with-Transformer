class C1(object):

    def crackSafe(self, a1, a2):
        """
        """
        v1 = [str(a2 - 1)] * (a1 - 1)
        v2 = set()
        v3 = a2 ** a1
        while len(v2) < v3:
            v4 = v1[len(v1) - a1 + 1:]
            for v5 in range(a2):
                v6 = ''.join(v4) + str(v5)
                if v6 not in v2:
                    v2.add(v6)
                    v1.append(str(v5))
                    break
        return ''.join(v1)
