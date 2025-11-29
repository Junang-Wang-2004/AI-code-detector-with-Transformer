class C1:

    def kthSmallest(self, a1, a2):

        def search(a1, a2):
            if not a1:
                return None
            v1 = search(a1.left, a2)
            if v1 is not None:
                return v1
            a2[0] -= 1
            if a2[0] == 0:
                return a1.val
            return search(a1.right, a2)
        return search(a1, [a2])
