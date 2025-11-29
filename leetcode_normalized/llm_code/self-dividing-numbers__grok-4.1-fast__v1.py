class C1(object):

    def selfDividingNumbers(self, a1, a2):
        v1 = []
        for v2 in range(a1, a2 + 1):
            v3 = v2
            v4 = True
            while v3 > 0:
                v5 = v3 % 10
                if v5 == 0 or v2 % v5 != 0:
                    v4 = False
                    break
                v3 //= 10
            if v4:
                v1.append(v2)
        return v1
