class C1(object):

    def makeFancyString(self, a1):
        v1 = []
        for v2 in a1:
            if len(v1) >= 2 and v1[-1] == v1[-2] == v2:
                continue
            v1.append(v2)
        return ''.join(v1)
