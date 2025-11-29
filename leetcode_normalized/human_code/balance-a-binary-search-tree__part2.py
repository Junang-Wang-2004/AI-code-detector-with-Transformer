class C1(object):

    def balanceBST(self, a1):
        """
        """

        def inorderTraversalHelper(a1, a2):
            if not a1:
                return
            inorderTraversalHelper(a1.left, a2)
            a2.append(a1.val)
            inorderTraversalHelper(a1.right, a2)

        def sortedArrayToBstHelper(a1, a2, a3):
            if a2 >= a3:
                return None
            v1 = a2 + (a3 - a2) // 2
            v2 = TreeNode(a1[v1])
            v2.left = sortedArrayToBstHelper(a1, a2, v1)
            v2.right = sortedArrayToBstHelper(a1, v1 + 1, a3)
            return v2
        v1 = []
        inorderTraversalHelper(a1, v1)
        return sortedArrayToBstHelper(v1, 0, len(v1))
