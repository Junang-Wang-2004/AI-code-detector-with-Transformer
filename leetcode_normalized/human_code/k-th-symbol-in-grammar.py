class C1(object):

    def kthGrammar(self, a1, a2):
        """
        """

        def bitCount(a1):
            v1 = 0
            while a1:
                a1 &= a1 - 1
                v1 += 1
            return v1
        return bitCount(a2 - 1) % 2
