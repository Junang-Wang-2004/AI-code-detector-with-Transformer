class C1(object):

    def minimizeResult(self, a1):
        """
        """
        v1 = None
        v2 = float('inf')
        v3 = a1.index('+')
        v4, v5 = (int(a1[0:v3]), int(a1[v3 + 1:]))
        v6, v7 = (10 ** v3, 10 ** (len(a1) - (v3 + 1) - 1))
        for v8 in range(v3):
            v9 = v7
            for v10 in range(v3 + 1, len(a1)):
                v11, v12 = divmod(v4, v6)
                v13, v14 = divmod(v5, v9)
                v15 = max(v11, 1) * (v12 + v13) * max(v14, 1)
                if v15 < v2:
                    v2 = v15
                    v1 = (v8, v10)
                v9 //= 10
            v6 //= 10
        return ''.join([a1[:v1[0]], '(', a1[v1[0]:v1[1] + 1], ')', a1[v1[1] + 1:]])
