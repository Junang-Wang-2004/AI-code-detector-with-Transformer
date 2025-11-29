class C1(object):

    def elementInNums(self, a1, a2):
        """
        """
        v1 = []
        for v2, v3 in a2:
            v2 %= 2 * len(a1)
            if v2 + v3 < len(a1):
                v1.append(a1[v2 + v3])
            elif v3 < v2 - len(a1):
                v1.append(a1[v3])
            else:
                v1.append(-1)
        return v1
