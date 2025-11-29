class C1(object):

    def maximumTime(self, a1):
        """
        """
        v1 = list(a1)
        for v2, v3 in enumerate(a1):
            if v3 != '?':
                continue
            if v2 == 0:
                v1[v2] = '2' if v1[v2 + 1] in '?0123' else '1'
            elif v2 == 1:
                v1[v2] = '3' if v1[0] == '2' else '9'
            elif v2 == 3:
                v1[v2] = '5'
            elif v2 == 4:
                v1[v2] = '9'
        return ''.join(v1)
