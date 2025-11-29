class C1:

    def __init__(self, a1=0, a2=None, a3=None):
        self.val = a1
        self.left = a2
        self.right = a3

class C2:

    def sumEvenGrandparent(self, a1):
        v1 = 0
        v2 = []
        if a1:
            v2.append((a1, None, None))
        while v2:
            v3, v4, v5 = v2.pop()
            if v5 is not None and v5 % 2 == 0:
                v1 += v3.val
            if v3.right:
                v2.append((v3.right, v3.val, v4))
            if v3.left:
                v2.append((v3.left, v3.val, v4))
        return v1
