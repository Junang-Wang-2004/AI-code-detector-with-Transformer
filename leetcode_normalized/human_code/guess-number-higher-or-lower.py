class C1(object):

    def guessNumber(self, a1):
        """
        """
        v1, v2 = (1, a1)
        while v1 <= v2:
            v3 = v1 + (v2 - v1) / 2
            if guess(v3) <= 0:
                v2 = v3 - 1
            else:
                v1 = v3 + 1
        return v1
