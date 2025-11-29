class C1:

    def findDuplicateSubtrees(self, a1):
        v1 = {}
        v2 = []

        def traverse(a1):
            if a1 is None:
                return None
            v1 = traverse(a1.left)
            v2 = traverse(a1.right)
            v3 = (a1.val, v1, v2)
            v1[v3] = v1.get(v3, 0) + 1
            if v1[v3] == 2:
                v2.append(a1)
            return v3
        traverse(a1)
        return v2
