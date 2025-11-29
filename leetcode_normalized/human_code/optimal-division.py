class C1(object):

    def optimalDivision(self, a1):
        """
        """
        if len(a1) == 1:
            return str(a1[0])
        if len(a1) == 2:
            return str(a1[0]) + '/' + str(a1[1])
        v1 = [str(a1[0]) + '/(' + str(a1[1])]
        for v2 in range(2, len(a1)):
            v1 += '/' + str(a1[v2])
        v1 += ')'
        return ''.join(v1)
