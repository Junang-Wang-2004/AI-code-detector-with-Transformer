class C1:

    def evaluateTree(self, a1):

        def process(a1):
            if a1.val <= 1:
                return a1.val
            v1 = process(a1.left)
            v2 = process(a1.right)
            if a1.val == 2:
                return v1 or v2
            return v1 and v2
        return process(a1)
