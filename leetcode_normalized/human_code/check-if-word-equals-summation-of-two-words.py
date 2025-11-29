class C1(object):

    def isSumEqual(self, a1, a2, a3):
        """
        """

        def stoi(a1):
            v1 = 0
            for v2 in a1:
                v1 = v1 * 10 + ord(v2) - ord('a')
            return v1
        return stoi(a1) + stoi(a2) == stoi(a3)
