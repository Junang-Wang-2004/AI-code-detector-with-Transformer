class C1(object):

    def diStringMatch(self, a1):
        """
        """
        v1 = []
        v2, v3 = (0, len(a1))
        for v4 in a1:
            if v4 == 'I':
                v1.append(v2)
                v2 += 1
            else:
                v1.append(v3)
                v3 -= 1
        v1.append(v2)
        return v1
