class C1(object):

    def minimizeResult(self, a1):
        """
        """
        v1 = None
        v2 = float('inf')
        v3 = a1.index('+')
        for v4 in range(v3):
            for v5 in range(v3 + 1, len(a1)):
                v6 = int(a1[:v4] or '1') * (int(a1[v4:v3]) + int(a1[v3 + 1:v5 + 1])) * int(a1[v5 + 1:] or '1')
                if v6 < v2:
                    v2 = v6
                    v1 = (v4, v5)
        return ''.join([a1[:v1[0]], '(', a1[v1[0]:v1[1] + 1], ')', a1[v1[1] + 1:]])
