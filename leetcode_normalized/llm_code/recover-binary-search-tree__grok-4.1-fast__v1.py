class C1:

    def __init__(self, a1=0, a2=None, a3=None):
        self.val = a1
        self.left = a2
        self.right = a3

class C2:

    def recoverTree(self, a1):
        v1 = []
        v2 = a1
        v3 = None
        v4 = None
        v5 = None
        while v1 or v2:
            while v2:
                v1.append(v2)
                v2 = v2.left
            v2 = v1.pop()
            if v3 and v3.val > v2.val:
                if v4 is None:
                    v4 = v3
                v5 = v2
            v3 = v2
            v2 = v2.right
        if v4:
            v4.val, v5.val = (v5.val, v4.val)
        return a1
