import collections
import fractions

class C1(object):

    def getCoprimes(self, a1, a2):
        """
        """

        def iter_dfs(a1, a2):
            v1 = [-1] * len(a1)
            v2 = collections.defaultdict(list)
            v3 = [(1, (-1, 0, 0))]
            while v3:
                v4, v5 = v3.pop()
                if v4 == 1:
                    v6, v7, v8 = v5
                    v3.append((4, (v7,)))
                    v3.append((3, (v6, v7, v8)))
                    v3.append((2, (v7,)))
                elif v4 == 2:
                    v7 = v5[0]
                    v9 = -1
                    for v10 in v2.keys():
                        if fractions.gcd(a1[v7], v10) != 1:
                            continue
                        if v2[v10][-1][1] > v9:
                            v9 = v2[v10][-1][1]
                            v1[v7] = v2[v10][-1][0]
                elif v4 == 3:
                    v6, v7, v8 = v5
                    v2[a1[v7]].append((v7, v8))
                    for v11 in a2[v7]:
                        if v11 == v6:
                            continue
                        v3.append((1, (v7, v11, v8 + 1)))
                elif v4 == 4:
                    v7 = v5[0]
                    v2[a1[v7]].pop()
                    if not v2[a1[v7]]:
                        v2.pop(a1[v7])
            return v1
        v1 = collections.defaultdict(list)
        for v2, v3 in a2:
            v1[v2].append(v3)
            v1[v3].append(v2)
        return iter_dfs(a1, v1)
