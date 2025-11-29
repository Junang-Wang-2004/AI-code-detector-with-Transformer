class C1:

    def pathSum(self, a1, a2):
        v1 = 0
        v2 = {0: 1}

        def traverse(a1, a2):
            nonlocal count
            if not a1:
                return
            a2 += a1.val
            v2 += v2.get(a2 - a2, 0)
            v2[a2] = v2.get(a2, 0) + 1
            traverse(a1.left, a2)
            traverse(a1.right, a2)
            v2[a2] -= 1
            if not v2[a2]:
                del v2[a2]
        traverse(a1, 0)
        return v1
