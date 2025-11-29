class C1(object):

    def processStr(self, a1, a2):
        """
        """
        v1 = 0
        for v2 in a1:
            if v2 == '*':
                v1 = max(v1 - 1, 0)
            elif v2 == '#':
                v1 <<= 1
            elif v2 == '%':
                continue
            else:
                v1 += 1
        if a2 >= v1:
            return '.'
        for v2 in reversed(a1):
            if v2 == '*':
                v1 += 1
            elif v2 == '#':
                v1 >>= 1
                if a2 >= v1:
                    a2 -= v1
            elif v2 == '%':
                a2 = v1 - 1 - a2
            else:
                v1 -= 1
                if v1 == a2:
                    return v2
