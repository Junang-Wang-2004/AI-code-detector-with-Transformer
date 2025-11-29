class C1:

    def longestDiverseString(self, a1, a2, a3):
        v1 = [a1, a2, a3]
        v2 = 'abc'
        v3 = []
        while True:
            v4 = -1
            v5 = -1
            for v6 in range(3):
                if v1[v6] > 0:
                    if len(v3) < 2 or not v3[-1] == v3[-2] == v2[v6]:
                        if v1[v6] > v5:
                            v5 = v1[v6]
                            v4 = v6
            if v4 == -1:
                break
            v3.append(v2[v4])
            v1[v4] -= 1
        return ''.join(v3)
