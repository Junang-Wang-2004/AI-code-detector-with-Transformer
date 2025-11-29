class C1(object):

    def missingInteger(self, a1):
        v1 = set(a1)
        v2 = 1
        while v2 in v1:
            v2 += 1
        return v2
