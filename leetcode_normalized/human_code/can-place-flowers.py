class C1(object):

    def canPlaceFlowers(self, a1, a2):
        """
        """
        for v1 in range(len(a1)):
            if a1[v1] == 0 and (v1 == 0 or a1[v1 - 1] == 0) and (v1 == len(a1) - 1 or a1[v1 + 1] == 0):
                a1[v1] = 1
                a2 -= 1
            if a2 <= 0:
                return True
        return False
