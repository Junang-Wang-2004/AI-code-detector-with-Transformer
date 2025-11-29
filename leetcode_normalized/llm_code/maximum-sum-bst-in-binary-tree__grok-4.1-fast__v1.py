class C1:

    def maxSumBST(self, a1):
        self.answer = 0

        def traverse(a1):
            if not a1:
                return (True, 0, float('inf'), float('-inf'))
            v1, v2, v3, v4 = traverse(a1.left)
            v5, v6, v7, v8 = traverse(a1.right)
            if v1 and v5 and (v4 < a1.val) and (a1.val < v7):
                v9 = v2 + a1.val + v6
                self.answer = max(self.answer, v9)
                return (True, v9, min(v3, a1.val), max(a1.val, v8))
            return (False, 0, 0, 0)
        traverse(a1)
        return self.answer
