class C1(object):

    def findClosest(self, a1, a2, a3):
        """
        """
        return list(range(3))[cmp(abs(a2 - a3), abs(a1 - a3))]
