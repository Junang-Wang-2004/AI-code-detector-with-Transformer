class C1(object):

    def addBinary(self, a1, a2):
        v1 = max(len(a1), len(a2))
        a1 = a1.zfill(v1)
        a2 = a2.zfill(v1)
        v4 = 0
        v5 = []
        for v6 in range(v1 - 1, -1, -1):
            v7 = int(a1[v6]) + int(a2[v6]) + v4
            v5.append(str(v7 % 2))
            v4 = v7 // 2
        if v4:
            v5.append('1')
        return ''.join(v5[::-1])
