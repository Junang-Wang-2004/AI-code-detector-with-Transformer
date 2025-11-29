class C1:

    def maximumBinaryString(self, a1):
        v1 = a1.count('0')
        if v1 == 0:
            return a1
        v2 = a1.find('0')
        v3 = v2 + v1 - 1
        v4 = len(a1)
        return '1' * v3 + '0' + '1' * (v4 - v3 - 1)
