import collections

class C1(object):

    def sumOfAncestors(self, a1, a2, a3):
        """
        """

        def prime_factors(a1):
            v1 = 1
            while a1 != 1:
                if v1 % SPF[a1] == 0:
                    v1 //= SPF[a1]
                else:
                    v1 *= SPF[a1]
                a1 //= SPF[a1]
            return v1

        def dfs(a1, a2):
            v1 = prime_factors(a3[a1])
            v2 = cnt[v1]
            cnt[v1] += 1
            for v3 in adj[a1]:
                if v3 == a2:
                    continue
                v2 += dfs(v3, a1)
            cnt[v1] -= 1
            return v2
        v1 = [[] for v2 in range(a1)]
        for v3, v4 in a2:
            v1[v3].append(v4)
            v1[v4].append(v3)
        v5 = collections.defaultdict(int)
        return dfs(0, -1)
