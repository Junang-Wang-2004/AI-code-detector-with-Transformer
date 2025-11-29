class C1(object):

    def getStrongest(self, a1, a2):
        """
        """
        a1.sort()
        v1 = a1[(len(a1) - 1) // 2]
        v2 = []
        v3, v4 = (0, len(a1) - 1)
        while len(v2) < a2:
            if v1 - a1[v3] > a1[v4] - v1:
                v2.append(a1[v3])
                v3 += 1
            else:
                v2.append(a1[v4])
                v4 -= 1
        return v2
