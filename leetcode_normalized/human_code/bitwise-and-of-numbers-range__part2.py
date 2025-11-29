class C1(object):

    def rangeBitwiseAnd(self, a1, a2):
        v1, v2 = (0, a2 - a1)
        while v2:
            v2 >>= 1
            v1 += 1
        return a2 & a1 >> v1 << v1
