import bisect

class C1(object):

    def closestNodes(self, a1, a2):
        """
        """

        def dfs(a1):
            if not a1:
                return
            dfs(a1.left)
            inorder.append(a1.val)
            dfs(a1.right)
        v1 = []
        dfs(a1)
        v2 = []
        for v3 in a2:
            v4 = bisect.bisect_left(v1, v3)
            if v4 == len(v1):
                v2.append([v1[v4 - 1], -1])
            elif v1[v4] == v3:
                v2.append([v1[v4], v1[v4]])
            elif v4 - 1 >= 0:
                v2.append([v1[v4 - 1], v1[v4]])
            else:
                v2.append([-1, v1[v4]])
        return v2
