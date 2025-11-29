class C1:

    def minDiffInBST(self, a1):
        v1 = []
        v2 = a1
        v3 = float('-inf')
        v4 = float('inf')
        while v1 or v2:
            while v2:
                v1.append(v2)
                v2 = v2.left
            v2 = v1.pop()
            v4 = min(v4, v2.val - v3)
            v3 = v2.val
            v2 = v2.right
        return v4
