class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def bstFromPreorder(self, a1):
        """
        """

        def bstFromPreorderHelper(a1, a2, a3, a4):
            if a4[0] == len(a1) or a1[a4[0]] < a2 or a1[a4[0]] > a3:
                return None
            v1 = C1(a1[a4[0]])
            a4[0] += 1
            v1.left = bstFromPreorderHelper(a1, a2, v1.val, a4)
            v1.right = bstFromPreorderHelper(a1, v1.val, a3, a4)
            return v1
        return bstFromPreorderHelper(a1, float('-inf'), float('inf'), [0])
