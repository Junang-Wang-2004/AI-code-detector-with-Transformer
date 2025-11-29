class C1:

    def equalToDescendants(self, a1):

        def traverse(a1):
            if not a1:
                return (0, 0)
            v1, v2 = traverse(a1.left)
            v3, v4 = traverse(a1.right)
            v5 = v2 + v4
            v6 = v1 + v3 + (1 if a1.val == v5 else 0)
            return (v6, v5 + a1.val)
        if not a1:
            return 0
        return traverse(a1)[0]
