import collections

class C1(object):

    def numSquarefulPerms(self, a1):
        """
        """

        def dfs(a1, a2, a3, a4, a5):
            a4[a2] -= 1
            if a3 == 0:
                a5[0] += 1
            for v1 in a1[a2]:
                if a4[v1]:
                    dfs(a1, v1, a3 - 1, a4, a5)
            a4[a2] += 1
        v1 = collections.Counter(a1)
        v2 = {i: {j for v3 in v1 if int((i + v3) ** 0.5) ** 2 == i + v3} for v4 in v1}
        v5 = [0]
        for v6 in v1:
            dfs(v2, v6, len(a1) - 1, v1, v5)
        return v5[0]
