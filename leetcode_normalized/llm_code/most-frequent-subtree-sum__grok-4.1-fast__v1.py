class C1:

    def findFrequentTreeSum(self, a1):
        v1 = {}

        def traverse(a1):
            if a1 is None:
                return 0
            v1 = traverse(a1.left)
            v2 = traverse(a1.right)
            v3 = a1.val + v1 + v2
            v1[v3] = v1.get(v3, 0) + 1
            return v3
        if a1 is not None:
            traverse(a1)
        if not v1:
            return []
        v2 = max(v1.values())
        v3 = [sum_val for v4, v5 in v1.items() if v5 == v2]
        return v3
