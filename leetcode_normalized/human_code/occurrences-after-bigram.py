class C1(object):

    def findOcurrences(self, a1, a2, a3):
        """
        """
        v1 = []
        a2 += ' '
        a3 += ' '
        v4 = []
        v5, v6, v7 = (0, 0, 0)
        while v7 < len(a1):
            v8 = a1[v7]
            v7 += 1
            if v5 != len(a2):
                if v8 == a2[v5]:
                    v5 += 1
                else:
                    v5 = 0
                continue
            if v6 != len(a3):
                if v8 == a3[v6]:
                    v6 += 1
                else:
                    v7 -= v6 + 1
                    v5, v6 = (0, 0)
                continue
            if v8 != ' ':
                v4.append(v8)
                continue
            v7 -= len(a3) + len(v4) + 1
            v5, v6 = (0, 0)
            v1.append(''.join(v4))
            v4 = []
        if v4:
            v1.append(''.join(v4))
        return v1
