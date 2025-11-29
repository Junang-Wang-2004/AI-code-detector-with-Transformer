class C1:

    def __init__(self, a1):
        self.val = a1
        self.left = self.right = None

class C2:

    def sortedArrayToBST(self, a1):

        def construct(a1, a2):
            if a1 >= a2:
                return None
            v1 = a1 + (a2 - a1) // 2
            v2 = C1(a1[v1])
            v2.left = construct(a1, v1)
            v2.right = construct(v1 + 1, a2)
            return v2
        return construct(0, len(a1))
