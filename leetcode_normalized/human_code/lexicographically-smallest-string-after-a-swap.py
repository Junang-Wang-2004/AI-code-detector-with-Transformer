class C1(object):

    def getSmallestString(self, a1):
        """
        """
        v1 = list(map(int, a1))
        for v2 in range(len(a1) - 1):
            if v1[v2] % 2 != v1[v2 + 1] % 2:
                continue
            if v1[v2] > v1[v2 + 1]:
                v1[v2], v1[v2 + 1] = (v1[v2 + 1], v1[v2])
                break
        return ''.join(map(str, v1))
