class C1(object):

    def recoverFromPreorder(self, a1):
        """
        """

        def recoverFromPreorderHelper(a1, a2, a3):
            v1 = a3[0]
            while v1 < len(a1) and a1[v1] == '-':
                v1 += 1
            if a2 != v1 - a3[0]:
                return None
            a3[0] = v1
            while v1 < len(a1) and a1[v1] != '-':
                v1 += 1
            v2 = TreeNode(int(a1[a3[0]:v1]))
            a3[0] = v1
            v2.left = recoverFromPreorderHelper(a1, a2 + 1, a3)
            v2.right = recoverFromPreorderHelper(a1, a2 + 1, a3)
            return v2
        return recoverFromPreorderHelper(a1, 0, [0])
