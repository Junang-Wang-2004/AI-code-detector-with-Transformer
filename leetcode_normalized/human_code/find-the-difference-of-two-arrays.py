class C1(object):

    def findDifference(self, a1, a2):
        """
        """
        v1 = [set(a1), set(a2)]
        return [list(v1[0] - v1[1]), list(v1[1] - v1[0])]
