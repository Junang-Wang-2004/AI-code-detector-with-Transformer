import collections

class C1(object):

    def distanceK(self, a1, a2, a3):
        """
        """

        def dfs(a1, a2, a3):
            if not a2:
                return
            if a1:
                a3[a1.val].append(a2.val)
                a3[a2.val].append(a1.val)
            dfs(a2, a2.left, a3)
            dfs(a2, a2.right, a3)
        v1 = collections.defaultdict(list)
        dfs(None, a1, v1)
        v2 = [a2.val]
        v3 = set(v2)
        for v4 in range(a3):
            v2 = [nei for v5 in v2 for v6 in v1[v5] if v6 not in v3]
            v3 |= set(v2)
        return v2
