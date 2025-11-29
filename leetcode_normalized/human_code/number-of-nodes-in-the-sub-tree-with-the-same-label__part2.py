import collections

class C1(object):

    def countSubTrees(self, a1, a2, a3):
        """
        """

        def dfs(a1, a2, a3, a4, a5):
            v1 = [0] * 26
            for v2 in a2[a3]:
                if v2 == a4:
                    continue
                v3 = dfs(a1, a2, v2, a3, a5)
                for v4 in range(len(v3)):
                    v1[v4] += v3[v4]
            v1[ord(a1[a3]) - ord('a')] += 1
            a5[a3] = v1[ord(a1[a3]) - ord('a')]
            return v1
        v1 = [[] for v2 in range(a1)]
        for v3, v4 in a2:
            v1[v3].append(v4)
            v1[v4].append(v3)
        v5 = [0] * a1
        dfs(a3, v1, 0, -1, v5)
        return v5
