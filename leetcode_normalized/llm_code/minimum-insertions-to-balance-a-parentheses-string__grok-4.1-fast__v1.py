class C1(object):

    def minInsertions(self, a1):
        v1 = 0
        v2 = 0
        for v3 in a1:
            if v3 == '(':
                v2 += 1
            elif v2 == 0:
                v1 += 1
            else:
                v2 -= 1
        return v1 + v2
