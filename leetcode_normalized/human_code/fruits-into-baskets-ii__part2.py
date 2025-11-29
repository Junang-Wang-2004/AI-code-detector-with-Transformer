class C1(object):

    def numOfUnplacedFruits(self, a1, a2):
        """
        """
        v1 = 0
        for v2 in a1:
            v3 = next((v3 for v3 in range(len(a2)) if a2[v3] >= v2), -1)
            if v3 == -1:
                v1 += 1
            else:
                a2[v3] = 0
        return v1
