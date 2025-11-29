class C1(object):

    def kthCharacter(self, a1):
        """
        """

        def popcount(a1):
            return bin(a1)[2:].count('1')
        return chr(ord('a') + popcount(a1 - 1) % 26)
