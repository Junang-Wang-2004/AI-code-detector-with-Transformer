import collections

class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def verticalTraversal(self, a1):
        """
        """

        def dfs(a1, a2, a3, a4):
            if not a1:
                return
            a2[a3][a4].append(a1)
            dfs(a1.left, a2, a3 - 1, a4 + 1)
            dfs(a1.right, a2, a3 + 1, a4 + 1)
        v1 = collections.defaultdict(lambda: collections.defaultdict(list))
        dfs(a1, v1, 0, 0)
        v2 = []
        for v3 in sorted(v1):
            v4 = []
            for v5 in sorted(v1[v3]):
                v4.extend(sorted((node.val for v6 in v1[v3][v5])))
            v2.append(v4)
        return v2
