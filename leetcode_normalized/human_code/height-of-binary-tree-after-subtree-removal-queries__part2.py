import collections

class C1(object):

    def treeQueries(self, a1, a2):
        """
        """

        def dfs(a1, a2):
            if not a1:
                return 0
            v1 = 1 + max(dfs(a1.left, a2 + 1), dfs(a1.right, a2 + 1))
            if v1 > top[a2][0]:
                top[a2][0], top[a2][1] = (v1, top[a2][0])
            elif v1 > top[a2][1]:
                top[a2][1] = v1
            depth[a1.val], height[a1.val] = (a2, v1)
            return v1
        v1 = collections.defaultdict(lambda: [0] * 2)
        v2, v3 = ({}, {})
        dfs(a1, 0)
        return [v2[q] - 1 + (v1[v2[q]][0] if v3[q] != v1[v2[q]][0] else v1[v2[q]][1]) for v4 in a2]
