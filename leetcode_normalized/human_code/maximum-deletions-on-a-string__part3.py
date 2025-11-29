class C1(object):

    def deleteString(self, a1):
        """
        """
        v1, v2 = (10 ** 9 + 7, (113, 109))

        def hash(a1, a2):
            return [(prefix[idx][a2 + 1] - prefix[idx][a1] * power[idx][a2 - a1 + 1]) % v1 for v1 in range(len(v2))]
        if all((x == a1[0] for v3 in a1)):
            return len(a1)
        v4 = [[1] for v5 in range(len(v2))]
        v6 = [[0] for v5 in range(len(v2))]
        for v3 in a1:
            for v7, v8 in enumerate(v2):
                v4[v7].append(v4[v7][-1] * v8 % v1)
                v6[v7].append((v6[v7][-1] * v8 + (ord(v3) - ord('a'))) % v1)
        v9 = [1] * len(a1)
        for v10 in reversed(range(len(a1) - 1)):
            for v11 in range(1, (len(a1) - v10) // 2 + 1):
                if hash(v10, v10 + v11 - 1) == hash(v10 + v11, v10 + 2 * v11 - 1):
                    v9[v10] = max(v9[v10], v9[v10 + v11] + 1)
        return v9[0]
