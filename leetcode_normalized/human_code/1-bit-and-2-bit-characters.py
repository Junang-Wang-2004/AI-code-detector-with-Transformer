class C1(object):

    def isOneBitCharacter(self, a1):
        """
        """
        v1 = 0
        for v2 in reversed(range(len(a1) - 1)):
            if a1[v2] == 0:
                break
            v1 ^= a1[v2]
        return v1 == 0
