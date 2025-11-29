class C1(object):

    def optimalDivision(self, a1):
        v1 = [str(val) for v2 in a1]
        v3 = len(v1)
        if v3 <= 2:
            return '/'.join(v1)
        return v1[0] + '/(' + '/'.join(v1[1:]) + ')'
