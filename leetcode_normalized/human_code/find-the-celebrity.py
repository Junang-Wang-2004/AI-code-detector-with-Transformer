class C1(object):

    def findCelebrity(self, a1):
        """
        """
        v1 = 0
        for v2 in range(1, a1):
            if knows(v1, v2):
                v1 = v2
        for v2 in range(a1):
            v3 = knows(v1, v2)
            v4 = knows(v2, v1)
            if v2 != v1 and (v3 or not v4):
                return -1
        return v1
