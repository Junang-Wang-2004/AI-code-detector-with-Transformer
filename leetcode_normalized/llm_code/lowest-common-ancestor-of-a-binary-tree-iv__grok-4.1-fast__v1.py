class C1:

    def lowestCommonAncestor(self, a1, a2):
        v1 = set(a2)
        v2 = len(targets_set)
        v3 = [None]

        def post_order_traverse(a1):
            if a1 is None:
                return 0
            v1 = post_order_traverse(a1.left)
            v2 = post_order_traverse(a1.right)
            v3 = 1 if a1 in v1 else 0
            v4 = v1 + v2 + v3
            if v4 == v2 and v3[0] is None:
                v3[0] = a1
            return v4
        post_order_traverse(a1)
        return v3[0]
