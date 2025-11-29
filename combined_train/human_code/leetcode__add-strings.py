class C1(object):

    def addStrings(self, a1, a2):
        """
        """
        v1 = []
        v2, v3, v4 = (len(a1) - 1, len(a2) - 1, 0)
        while v2 >= 0 or v3 >= 0 or v4:
            if v2 >= 0:
                v4 += ord(a1[v2]) - ord('0')
                v2 -= 1
            if v3 >= 0:
                v4 += ord(a2[v3]) - ord('0')
                v3 -= 1
            v1.append(str(v4 % 10))
            v4 /= 10
        v1.reverse()
        return ''.join(v1)

    def addStrings2(self, a1, a2):
        """
        """
        v1 = max(len(a1), len(a2))
        a1 = a1.zfill(v1)[::-1]
        a2 = a2.zfill(v1)[::-1]
        v4, v5 = ('', 0)
        for v6, v7 in enumerate(a1):
            v8 = str(int(v7) + int(a2[v6]) + v5)
            v4 += v8[-1]
            if int(v8) > 9:
                v5 = 1
            else:
                v5 = 0
        if v5:
            v4 += '1'
        return v4[::-1]
