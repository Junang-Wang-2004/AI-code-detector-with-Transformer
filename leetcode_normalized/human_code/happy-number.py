class C1(object):

    def isHappy(self, a1):
        v1 = {}
        while a1 != 1 and a1 not in v1:
            v1[a1] = True
            a1 = self.nextNumber(a1)
        return a1 == 1

    def nextNumber(self, a1):
        v1 = 0
        for v2 in str(a1):
            v1 += int(v2) ** 2
        return v1
