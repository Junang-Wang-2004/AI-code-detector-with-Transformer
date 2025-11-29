class C1(object):

    def isRectangleOverlap(self, a1, a2):
        """
        """

        def intersect(a1, a2, a3, a4):
            return max(a1, a3) < min(a2, a4)
        return intersect(a1[0], a1[2], a2[0], a2[2]) and intersect(a1[1], a1[3], a2[1], a2[3])
