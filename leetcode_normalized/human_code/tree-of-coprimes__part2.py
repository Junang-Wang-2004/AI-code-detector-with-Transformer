import collections
import fractions

class C1(object):

    def getCoprimes(self, a1, a2):
        """
        """

        def dfs(a1, a2, a3, a4, a5, a6, a7):
            v1 = -1
            for v2 in a6.keys():
                if fractions.gcd(a1[a4], v2) != 1:
                    continue
                if a6[v2][-1][1] > v1:
                    v1 = a6[v2][-1][1]
                    a7[a4] = a6[v2][-1][0]
            a6[a1[a4]].append((a4, a5))
            for v3 in a2[a4]:
                if v3 == a3:
                    continue
                dfs(a1, a2, a4, v3, a5 + 1, a6, a7)
            a6[a1[a4]].pop()
            if not a6[a1[a4]]:
                a6.pop(a1[a4])
        v1 = collections.defaultdict(list)
        for v2, v3 in a2:
            v1[v2].append(v3)
            v1[v3].append(v2)
        v4 = [-1] * len(a1)
        v5 = collections.defaultdict(list)
        dfs(a1, v1, -1, 0, 0, v5, v4)
        return v4
