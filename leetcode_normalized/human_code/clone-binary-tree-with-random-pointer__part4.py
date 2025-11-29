import collections

class C1(object):

    def copyRandomBinaryTree(self, a1):
        """
        """

        def dfs(a1, a2):
            if not a1:
                return
            a2[a1].val = a1.val
            a2[a1].left = a2[a1.left]
            a2[a1].right = a2[a1.right]
            a2[a1].random = a2[a1.random]
            dfs(a1.left, a2)
            dfs(a1.right, a2)
        v1 = collections.defaultdict(lambda: NodeCopy())
        v1[None] = None
        dfs(a1, v1)
        return v1[a1]
