import collections

class C1(object):

    def maxAmount(self, a1, a2, a3, a4, a5):
        """
        """

        def find_adj(a1, a2):
            v1 = collections.defaultdict(list)
            for v2 in range(len(a1)):
                v1[a1[v2][0]].append((a1[v2][1], a2[v2]))
                v1[a1[v2][1]].append((a1[v2][0], 1 / a2[v2]))
            return v1

        def bfs(a1, a2):
            v1 = list(a1.keys())
            while v1:
                v2 = []
                for v3 in v1:
                    for v4, v5 in a2[v3]:
                        if not v5 * a1[v3] > a1[v4]:
                            continue
                        a1[v4] = v5 * a1[v3]
                        v2.append(v4)
                v1 = v2
            return a1
        v1 = collections.defaultdict(int)
        v1[a1] = 1.0
        v2 = find_adj(a2, a3)
        bfs(v1, v2)
        v3 = find_adj(a4, a5)
        bfs(v1, v3)
        return v1[a1]
