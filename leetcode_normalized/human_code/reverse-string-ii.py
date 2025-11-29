class C1(object):

    def reverseStr(self, a1, a2):
        """
        """
        a1 = list(a1)
        for v2 in range(0, len(a1), 2 * a2):
            a1[v2:v2 + a2] = reversed(a1[v2:v2 + a2])
        return ''.join(a1)
