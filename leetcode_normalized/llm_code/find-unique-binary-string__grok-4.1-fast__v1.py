class C1:

    def findDifferentBinaryString(self, a1):
        v1 = len(a1)
        v2 = []
        for v3 in range(v1):
            v4 = a1[v3][v3]
            v2.append('1' if v4 == '0' else '0')
        return ''.join(v2)
