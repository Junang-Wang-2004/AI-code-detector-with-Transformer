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

        def dfs(a1, a2):
            v1 = [1 - is_prime(a1 + 1), is_prime(a1 + 1)]
            for v2 in adj[a1]:
                if v2 == a2:
                    continue
                v3 = dfs(v2, a1)
                result[0] += v1[0] * v3[1] + v1[1] * v3[0]
                if is_prime(a1 + 1):
                    v1[1] += v3[0]
                else:
                    v1[0] += v3[0]
                    v1[1] += v3[1]
            return v1
        v1 = linear_sieve_of_eratosthenes(a1)
        v2 = [[] for v3 in range(a1)]
        for v4, v5 in a2:
            v4, v5 = (v4 - 1, v5 - 1)
            v2[v4].append(v5)
            v2[v5].append(v4)
        v6 = [0]
        dfs(0, -1)
        return v6[0]
