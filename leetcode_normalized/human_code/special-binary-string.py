class C1(object):

    def makeLargestSpecial(self, a1):
        """
        """
        v1 = []
        v2 = v3 = 0
        for v4, v5 in enumerate(a1):
            v3 += 1 if v5 == '1' else -1
            if v3 == 0:
                v1.append('1{}0'.format(self.makeLargestSpecial(a1[v2 + 1:v4])))
                v2 = v4 + 1
        v1.sort(reverse=True)
        return ''.join(v1)
