class C1:

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2:

    def __init__(self, a1):
        self.root = a1

    def find(self, a1):
        v1 = self.root
        v2 = a1
        v3 = []
        while v2 > 0:
            v3.append(v2 % 2 == 0)
            v2 = (v2 - 1) // 2
        for v4 in reversed(v3):
            if v4:
                if not v1 or not v1.right:
                    return False
                v1 = v1.right
            else:
                if not v1 or not v1.left:
                    return False
                v1 = v1.left
        return v1 is not None
