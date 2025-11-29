class C1:

    def subtreeWithAllDeepest(self, a1):

        def recurse(a1):
            if not a1:
                return (None, 0)
            v1, v2 = recurse(a1.left)
            v3, v4 = recurse(a1.right)
            v5 = max(v2, v4)
            if v2 == v5 == v4:
                return (a1, v5 + 1)
            if v2 == v5:
                return (v1, v5 + 1)
            return (v3, v5 + 1)
        return recurse(a1)[0]
