class C1:

    def __init__(self, a1=0, a2=None, a3=None):
        self.val = a1
        self.left = a2
        self.right = a3

class C2:

    def minCameraCover(self, a1):
        v1 = 0

        def postorder(a1):
            nonlocal count
            if a1 is None:
                return 1
            v1 = postorder(a1.left)
            v2 = postorder(a1.right)
            if v1 == 0 or v2 == 0:
                v3 += 1
                return 2
            elif v1 == 2 or v2 == 2:
                return 1
            return 0
        v2 = postorder(a1)
        if v2 == 0:
            v1 += 1
        return v1
