class C1(object):

    def findBall(self, a1):
        """
        """
        v1 = []
        for v2 in range(len(a1[0])):
            for v3 in range(len(a1)):
                v4 = v2 + a1[v3][v2]
                if not (0 <= v4 < len(a1[0]) and a1[v3][v4] == a1[v3][v2]):
                    v2 = -1
                    break
                v2 = v4
            v1.append(v2)
        return v1
