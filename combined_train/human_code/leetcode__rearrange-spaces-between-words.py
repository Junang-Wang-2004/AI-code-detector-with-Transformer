class C1(object):

    def reorderSpaces(self, a1):
        """
        """
        a1 = list(a1)
        v2, v3 = (0, 0)
        for v4, v5 in enumerate(a1):
            if v5 == ' ':
                v2 += 1
            elif v4 == 0 or a1[v4 - 1] == ' ':
                v3 += 1
        v6, v4 = (0, 0)
        while v4 < len(a1):
            v7 = False
            while v4 < len(a1) and a1[v4] != ' ':
                a1[v6], a1[v4] = (a1[v4], a1[v6])
                v6 += 1
                v4 += 1
                v7 = True
            if v7:
                v6 += 1
            v4 += 1
        v8 = v2 // (v3 - 1) if v3 - 1 > 0 else 0
        v9 = v2 % (v3 - 1) if v3 - 1 > 0 else v2
        v10, v4 = (len(a1) - 1 - v9, len(a1) - 1)
        while v4 >= 0:
            v7 = False
            while v4 >= 0 and a1[v4] != ' ':
                a1[v10], a1[v4] = (a1[v4], a1[v10])
                v10 -= 1
                v4 -= 1
                v7 = True
            if v7:
                v10 -= v8
            v4 -= 1
        return ''.join(a1)
