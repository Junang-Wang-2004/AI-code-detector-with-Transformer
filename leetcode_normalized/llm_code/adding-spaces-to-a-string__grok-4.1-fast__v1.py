class C1(object):

    def addSpaces(self, a1, a2):
        v1 = []
        v2 = 0
        v3 = len(a2)
        for v4, v5 in enumerate(a1):
            while v2 < v3 and a2[v2] == v4:
                v1.append(' ')
                v2 += 1
            v1.append(v5)
        return ''.join(v1)
