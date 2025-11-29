class C1(object):

    def processStr(self, a1):
        v1 = []
        for v2 in a1:
            if v2 == '*':
                if v1:
                    v1.pop()
            elif v2 == '#':
                v1.extend(v1)
            elif v2 == '%':
                v1.reverse()
            else:
                v1.append(v2)
        return ''.join(v1)
