class C1:

    def createBinaryTree(self, a1):
        v1 = set()
        v2 = set()
        for v3, v4, v5 in a1:
            v1.add(v3)
            v1.add(v4)
            v2.add(v4)
        v6 = (v1 - v2).pop()
        v7 = {v: TreeNode(v) for v8 in v1}
        for v3, v4, v5 in a1:
            v9 = v7[v3]
            v10 = v7[v4]
            if v5:
                v9.left = v10
            else:
                v9.right = v10
        return v7[v6]
