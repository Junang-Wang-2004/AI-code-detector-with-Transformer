class C1(object):

    def createBinaryTree(self, a1):
        """
        """
        v1 = {}
        v2 = set()
        for v3, v4, v5 in a1:
            v6 = v1.setdefault(v3, TreeNode(v3))
            v7 = v1.setdefault(v4, TreeNode(v4))
            if v5:
                v6.left = v7
            else:
                v6.right = v7
            v2.add(v4)
        return v1[next((v3 for v3 in v1.keys() if v3 not in v2))]
