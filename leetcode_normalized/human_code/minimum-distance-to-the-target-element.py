class C1(object):

    def getMinDistance(self, a1, a2, a3):
        """
        """
        for v1 in range(len(a1)):
            if a3 - v1 >= 0 and a1[a3 - v1] == a2 or (a3 + v1 < len(a1) and a1[a3 + v1] == a2):
                break
        return v1
