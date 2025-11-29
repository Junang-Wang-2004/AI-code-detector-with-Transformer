class C1(object):

    def isUgly(self, a1):
        if a1 == 0:
            return False
        for v1 in [2, 3, 5]:
            while a1 % v1 == 0:
                a1 /= v1
        return a1 == 1
