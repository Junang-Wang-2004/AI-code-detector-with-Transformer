class C1(object):

    def addNegabinary(self, a1, a2):
        """
        """
        v1 = []
        v2 = 0
        while a1 or a2 or v2:
            if a1:
                v2 += a1.pop()
            if a2:
                v2 += a2.pop()
            v1.append(v2 & 1)
            v2 = -(v2 >> 1)
        while len(v1) > 1 and v1[-1] == 0:
            v1.pop()
        v1.reverse()
        return v1
