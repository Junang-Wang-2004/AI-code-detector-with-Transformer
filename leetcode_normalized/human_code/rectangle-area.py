class C1(object):

    def computeArea(self, a1, a2, a3, a4, a5, a6, a7, a8):
        return (a4 - a2) * (a3 - a1) + (a7 - a5) * (a8 - a6) - max(0, min(a3, a7) - max(a1, a5)) * max(0, min(a4, a8) - max(a2, a6))
