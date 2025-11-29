class C1(object):

    def findComplement(self, a1):
        v1 = 1
        while v1 <= a1:
            v1 <<= 1
        return v1 - 1 ^ a1
