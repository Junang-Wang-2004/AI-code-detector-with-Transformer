class C1:

    def findSecondMinimumValue(self, a1):
        v1 = float('inf')
        v2 = float('inf')

        def traverse(a1):
            nonlocal first, second
            if not a1:
                return
            if a1.val < v1:
                v1 = v1
                v2 = a1.val
            elif a1.val > v2 and a1.val < v1:
                v1 = a1.val
            traverse(a1.left)
            traverse(a1.right)
        traverse(a1)
        return v2 if v2 != float('inf') else -1
