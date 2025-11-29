class C1(object):

    def parseTernary(self, a1):
        """
        """
        if not a1:
            return ''
        v1 = []
        for v2 in a1[::-1]:
            if v1 and v1[-1] == '?':
                v1.pop()
                v3 = v1.pop()
                v1.pop()
                v4 = v1.pop()
                if v2 == 'T':
                    v1.append(v3)
                else:
                    v1.append(v4)
            else:
                v1.append(v2)
        return str(v1[-1])
