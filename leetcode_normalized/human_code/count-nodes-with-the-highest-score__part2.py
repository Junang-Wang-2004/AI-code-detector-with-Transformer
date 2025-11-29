from functools import reduce

class C1(object):

    def countHighestScoreNodes(self, a1):
        """
        """

        def dfs(a1, a2, a3):
            v1 = [dfs(a1, child, a3) for v2 in a1[a2]]
            v3 = sum(v1) + 1
            v4 = max(len(a1) - v3, 1) * reduce(lambda x, y: x * y, v1, 1)
            if v4 > a3[0]:
                a3[:] = [v4, 1]
            elif v4 == a3[0]:
                a3[1] += 1
            return v3
        v1 = [[] for v2 in range(len(a1))]
        for v3 in range(1, len(a1)):
            v1[a1[v3]].append(v3)
        v4 = [0] * 2
        dfs(v1, 0, v4)
        return v4[1]
