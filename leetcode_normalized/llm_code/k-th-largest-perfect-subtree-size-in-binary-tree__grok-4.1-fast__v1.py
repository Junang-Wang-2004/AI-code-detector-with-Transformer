class C1:

    def kthLargestPerfectSubtree(self, a1, a2):
        v1 = []

        def evaluate(a1):
            if not a1:
                return 0
            v1 = evaluate(a1.left)
            v2 = evaluate(a1.right)
            v3 = v1 + v2 + 1 if v1 == v2 >= 0 else -1
            v1.append(v3)
            return v3
        evaluate(a1)
        v2 = sorted((s for v3 in v1 if v3 > 0))[::-1]
        return v2[a2 - 1] if a2 <= len(v2) else -1
