class C1(object):

    def countPaths(self, a1, a2):
        """
        """

        def linear_sieve_of_eratosthenes(a1):
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

        def is_prime(a1):
            return spf[a1] == a1

        def iter_dfs():
            v1 = 0
            v2 = [(1, (0, -1, [0] * 2))]
            while v2:
                v3, v4 = v2.pop()
                if v3 == 1:
                    v5, v6, v7 = v4
                    v7[:] = [1 - is_prime(v5 + 1), is_prime(v5 + 1)]
                    v2.append((2, (v5, v6, v7, 0)))
                elif v3 == 2:
                    v5, v6, v7, v8 = v4
                    if v8 == len(adj[v5]):
                        continue
                    v9 = adj[v5][v8]
                    v2.append((2, (v5, v6, v7, v8 + 1)))
                    if v9 == v6:
                        continue
                    v10 = [0] * 2
                    v2.append((3, (v5, v6, v10, v7, v8)))
                    v2.append((1, (v9, v5, v10)))
                elif v3 == 3:
                    v5, v6, v10, v7, v8 = v4
                    v1 += v7[0] * v10[1] + v7[1] * v10[0]
                    if is_prime(v5 + 1):
                        v7[1] += v10[0]
                    else:
                        v7[0] += v10[0]
                        v7[1] += v10[1]
            return v1
        v1 = linear_sieve_of_eratosthenes(a1)
        v2 = [[] for v3 in range(a1)]
        for v4, v5 in a2:
            v4, v5 = (v4 - 1, v5 - 1)
            v2[v4].append(v5)
            v2[v5].append(v4)
        return iter_dfs()
