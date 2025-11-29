class C1(object):

    def minMaxGame(self, a1):
        """
        """
        v1 = a1[:]
        while len(v1) != 1:
            v2 = []
            for v3 in range(len(v1) // 2):
                v2.append(min(v1[2 * v3], v1[2 * v3 + 1]) if v3 % 2 == 0 else max(v1[2 * v3], v1[2 * v3 + 1]))
            v1 = v2
        return v1[0]
