class C1(object):

    def getSum(self, a1):
        v1 = 10 ** 9 + 7

        def process(a1):
            v1 = 0
            v2 = 0
            v3 = 0
            for v4 in range(len(a1)):
                if v2 == 0 or a1[v4] - a1[v4 - 1] != a1:
                    v2 = 1
                    v3 = a1[v4] * 1 % v1
                    v1 = (v1 + v3) % v1
                else:
                    v2 += 1
                    v3 = (v3 + a1[v4] * v2 % v1) % v1
                    v1 = (v1 + v3) % v1
            return v1
        v2 = 0
        for v3 in a1:
            v2 = (v2 + v3) % v1
        v4 = process(1)
        v5 = process(-1)
        return (v4 + v5 - v2 + v1) % v1
