import collections

class C1(object):

    def minMaxWeight(self, a1, a2, a3):
        """
        """

        def binary_search(a1, a2, a3):
            while a1 <= a2:
                v1 = a1 + (a2 - a1) // 2
                if a3(v1):
                    a2 = v1 - 1
                else:
                    a1 = v1 + 1
            return a1

        def check(a1):
            v1 = len(adj)
            v2 = [False] * len(adj)
            v2[0] = True
            v1 -= 1
            v3 = [0]
            while v3:
                v4 = []
                for v5 in v3:
                    for v6, v7 in adj[v5].items():
                        if v7 > a1 or v2[v6]:
                            continue
                        v2[v6] = True
                        v1 -= 1
                        v4.append(v6)
                v3 = v4
            return v1 == 0
        v1 = [collections.defaultdict(lambda: float('inf')) for v2 in range(a1)]
        for v3, v4, v5 in a2:
            v1[v4][v3] = min(v1[v4][v3], v5)
        v6, v7 = (min((v5 for v2, v2, v5 in a2)), max((v5 for v2, v2, v5 in a2)))
        v8 = binary_search(v6, v7, check)
        return v8 if v8 <= v7 else -1
