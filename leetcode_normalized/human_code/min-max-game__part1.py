class C1(object):

    def minMaxGame(self, a1):
        """
        """
        v1 = len(a1)
        while v1 != 1:
            v2 = []
            for v3 in range(v1 // 2):
                a1[v3] = min(a1[2 * v3], a1[2 * v3 + 1]) if v3 % 2 == 0 else max(a1[2 * v3], a1[2 * v3 + 1])
            v1 //= 2
        return a1[0]
