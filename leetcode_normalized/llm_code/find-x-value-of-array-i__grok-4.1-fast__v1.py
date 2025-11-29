class C1(object):

    def resultArray(self, a1, a2):
        v1 = [0] * a2
        v2 = {}
        for v3 in a1:
            v4 = v3 % a2
            v5 = {v4: 1}
            for v6, v7 in v2.items():
                v8 = v6 * v4 % a2
                v5[v8] = v5.get(v8, 0) + v7
            for v9, v10 in v5.items():
                v1[v9] += v10
            v2 = v5
        return v1
