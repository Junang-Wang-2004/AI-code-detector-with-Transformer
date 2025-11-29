class C1(object):

    def getFactors(self, a1):
        v1 = []
        v2 = []
        self.getResult(a1, v1, v2)
        return v1

    def getResult(self, a1, a2, a3):
        v1 = 2 if not a3 else a3[-1]
        while v1 <= a1 / v1:
            if a1 % v1 == 0:
                a3.append(v1)
                a3.append(a1 / v1)
                a2.append(list(a3))
                a3.pop()
                self.getResult(a1 / v1, a2, a3)
                a3.pop()
            v1 += 1
