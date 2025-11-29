class C1(object):

    def clearDigits(self, a1):
        """
        """
        a1 = list(a1)
        v2 = 0
        for v3, v4 in enumerate(a1):
            if v4.isdigit():
                v2 -= 1
                continue
            a1[v2] = v4
            v2 += 1
        while len(a1) > v2:
            a1.pop()
        return ''.join(a1)
