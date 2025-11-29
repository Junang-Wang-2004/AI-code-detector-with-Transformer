class C1:

    def getNoZeroIntegers(self, a1):
        for v1 in range(1, a1):
            v2 = a1 - v1
            if '0' not in str(v1) and '0' not in str(v2):
                return [v1, v2]
