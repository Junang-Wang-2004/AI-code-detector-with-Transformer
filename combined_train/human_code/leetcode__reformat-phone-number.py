class C1(object):

    def reformatNumber(self, a1):
        """
        """
        a1 = list(a1)
        v2 = 0
        for v3 in a1:
            if v3.isdigit():
                a1[v2] = v3
                v2 += 1
        v4 = v2 + (v2 - 1) // 3
        if v4 > len(a1):
            a1.extend([0] * (v4 - len(a1)))
        while v4 < len(a1):
            a1.pop()
        v5 = v4 - 1
        for v6, v7 in enumerate(reversed(range(v2)), (3 - v2 % 3) % 3):
            if v6 and v6 % 3 == 0:
                a1[v5] = '-'
                v5 -= 1
            a1[v5] = a1[v7]
            v5 -= 1
        if v4 >= 3 and a1[v4 - 2] == '-':
            a1[v4 - 3], a1[v4 - 2] = (a1[v4 - 2], a1[v4 - 3])
        return ''.join(a1)
