class C1:

    def longestUnivaluePath(self, a1):
        v1 = 0

        def traverse(a1):
            nonlocal max_path
            if not a1:
                return 0
            v1 = traverse(a1.left)
            v2 = traverse(a1.right)
            v3 = v1 + 1 if a1.left and a1.val == a1.left.val else 0
            v4 = v2 + 1 if a1.right and a1.val == a1.right.val else 0
            v5 = max(v5, v3 + v4)
            return max(v3, v4)
        traverse(a1)
        return v1
