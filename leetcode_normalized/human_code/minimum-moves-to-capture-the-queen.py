class C1(object):

    def minMovesToCaptureTheQueen(self, a1, a2, a3, a4, a5, a6):
        """
        """
        if a1 == a5 and (not (a1 == a3 and (a2 - a4) * (a6 - a4) < 0)):
            return 1
        if a2 == a6 and (not (a2 == a4 and (a1 - a3) * (a5 - a3) < 0)):
            return 1
        if a3 + a4 == a5 + a6 and (not (a3 + a4 == a1 + a2 and (a3 - a1) * (a5 - a1) < 0)):
            return 1
        if a3 - a4 == a5 - a6 and (not (a3 - a4 == a1 - a2 and (a4 - a2) * (a6 - a2) < 0)):
            return 1
        return 2
