class C1:

    def findComplement(self, a1):
        v1 = a1.bit_length()
        v2 = (1 << v1) - 1
        return v2 ^ a1
