class C1(object):

    def compressedString(self, a1):
        """
        """
        v1 = []
        v2 = 0
        for v3 in range(len(a1)):
            v2 += 1
            if v2 == 9 or (v3 + 1 == len(a1) or a1[v3 + 1] != a1[v3]):
                v1.append('%s%s' % (v2, a1[v3]))
                v2 = 0
        return ''.join(v1)
