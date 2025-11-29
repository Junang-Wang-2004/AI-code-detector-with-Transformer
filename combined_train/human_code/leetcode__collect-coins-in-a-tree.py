class C1(object):

    def collectTheCoins(self, a1, a2):
        """
        """
        v1 = 2
        v2 = [set() for v3 in range(len(a1))]
        for v4, v5 in a2:
            v2[v4].add(v5)
            v2[v5].add(v4)
        v6 = len(a1)
        v7 = []
        for v4 in range(len(a1)):
            while len(v2[v4]) == 1 and (not a1[v4]):
                v5 = v2[v4].pop()
                v2[v5].remove(v4)
                v6 -= 1
                v4 = v5
        v7 = [v4 for v4 in range(len(a1)) if len(v2[v4]) == 1]
        for v3 in range(v1):
            v8 = []
            for v4 in v7:
                if not v2[v4]:
                    assert v6 == 1
                    break
                v5 = v2[v4].pop()
                v2[v5].remove(v4)
                v6 -= 1
                if len(v2[v5]) == 1:
                    v8.append(v5)
            v7 = v8
        return (v6 - 1) * 2
