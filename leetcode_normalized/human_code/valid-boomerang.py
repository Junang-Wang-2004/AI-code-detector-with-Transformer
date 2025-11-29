class C1(object):

    def isBoomerang(self, a1):
        """
        """
        return (a1[0][0] - a1[1][0]) * (a1[0][1] - a1[2][1]) - (a1[0][0] - a1[2][0]) * (a1[0][1] - a1[1][1]) != 0
