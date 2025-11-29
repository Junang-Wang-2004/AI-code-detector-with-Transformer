class C1(object):

    def rangeBitwiseAnd(self, a1, a2):
        while a1 < a2:
            a2 &= a2 - 1
        return a2
