class C1:

    def pseudoPalindromicPaths(self, a1: TreeNode) -> int:

        def traverse(a1: TreeNode, a2: int) -> int:
            if not a1:
                return 0
            a2 ^= 1 << a1.val - 1
            if not a1.left and (not a1.right):
                return 1 if a2 & a2 - 1 == 0 else 0
            v2 = 0
            if a1.left:
                v2 += traverse(a1.left, a2)
            if a1.right:
                v2 += traverse(a1.right, a2)
            return v2
        return traverse(a1, 0)
