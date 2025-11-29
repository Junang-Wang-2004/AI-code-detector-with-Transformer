class C1(object):

    def crackSafe(self, a1, a2):
        """
        """
        v1 = a2 ** a1
        v2 = v1 // a2
        v3 = 0
        v4 = [str(0)] * (a1 - 1)
        v5 = set()
        while len(v5) < v1:
            for v6 in reversed(range(a2)):
                v7 = v3 * a2 + v6
                if v7 not in v5:
                    v5.add(v7)
                    v4.append(str(v6))
                    v3 = v7 % v2
                    break
        return ''.join(v4)
