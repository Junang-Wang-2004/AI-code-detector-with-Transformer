class C1(object):

    def minimumTimeToInitialState(self, a1, a2):
        v1 = len(a1)
        v2 = 1000000007
        v3 = 1000000009
        v4 = 131
        v5 = 137
        v6 = [0] * (v1 + 1)
        v7 = [0] * (v1 + 1)
        v8 = [1] * (v1 + 1)
        v9 = [1] * (v1 + 1)
        for v10 in range(v1):
            v11 = ord(a1[v10])
            v6[v10 + 1] = (v6[v10] * v4 + v11) % v2
            v7[v10 + 1] = (v7[v10] * v5 + v11) % v3
            v8[v10 + 1] = v8[v10] * v4 % v2
            v9[v10 + 1] = v9[v10] * v5 % v3

        def get_hash(a1, a2):
            v1 = (v6[a2] - v6[a1] * v8[a2 - a1] % v2 + v2) % v2
            v2 = (v7[a2] - v7[a1] * v9[a2 - a1] % v3 + v3) % v3
            return (v1, v2)
        for v12 in range(a2, v1 + 1, a2):
            v13 = v1 - v12
            if get_hash(v12, v1) == get_hash(0, v13):
                return v12 // a2
        return (v1 + a2 - 1) // a2
