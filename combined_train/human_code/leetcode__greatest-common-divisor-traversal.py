def f1(a1):
    v1 = []
    v2 = [-1] * (a1 + 1)
    for v3 in range(2, a1 + 1):
        if v2[v3] == -1:
            v2[v3] = v3
            v1.append(v3)
        for v4 in v1:
            if v3 * v4 > a1 or v4 > v2[v3]:
                break
            v2[v3 * v4] = v4
    return v1
v1 = 10 ** 5
v2 = f1(int(v1 ** 0.5))

class C1(object):

    def canTraverseAllPairs(self, a1):
        """
        """

        def prime_factors(a1):
            v1 = collections.Counter()
            for v2 in v2:
                if v2 * v2 > a1:
                    break
                while a1 % v2 == 0:
                    v1[v2] += 1
                    a1 //= v2
            if a1 != 1:
                v1[a1] += 1
            return v1

        def bfs():
            v1 = [False] * len(a1)
            v1[0] = True
            v2 = [0]
            while v2:
                v3 = []
                for v4 in v2:
                    for v5 in adj[v4]:
                        if v1[v5]:
                            continue
                        v1[v5] = True
                        v3.append(v5)
                v2 = v3
            return all(v1)
        v1 = [[] for v2 in range(len(a1))]
        v3 = {}
        for v4, v5 in enumerate(a1):
            for v6 in prime_factors(v5):
                if v6 not in v3:
                    v3[v6] = v4
                    continue
                v1[v4].append(v3[v6])
                v1[v3[v6]].append(v4)
        return bfs()
