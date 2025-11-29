import collections

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
    return v2
v1 = 10 ** 5
v2 = f1(v1)

class C1(object):

    def sumOfAncestors(self, a1, a2, a3):
        """
        """

        def prime_factors(a1):
            v1 = 1
            while a1 != 1:
                if v1 % v2[a1] == 0:
                    v1 //= v2[a1]
                else:
                    v1 *= v2[a1]
                a1 //= v2[a1]
            return v1

        def iter_dfs():
            v1 = 0
            v2 = [(1, (0, -1))]
            while v2:
                v3, v4 = v2.pop()
                if v3 == 1:
                    v5, v6 = v4
                    v7 = prime_factors(a3[v5])
                    v1 += cnt[v7]
                    cnt[v7] += 1
                    v2.append((3, (v7,)))
                    v2.append((2, (v5, v6, 0)))
                elif v3 == 2:
                    v5, v6, v8 = v4
                    if v8 == len(adj[v5]):
                        continue
                    v2.append((2, (v5, v6, v8 + 1)))
                    v9 = adj[v5][v8]
                    if v9 == v6:
                        continue
                    v2.append((1, (v9, v5)))
                elif v3 == 3:
                    v7 = v4[0]
                    cnt[v7] -= 1
            return v1
        v1 = [[] for v2 in range(a1)]
        for v3, v4 in a2:
            v1[v3].append(v4)
            v1[v4].append(v3)
        v5 = collections.defaultdict(int)
        return iter_dfs()
