class C1:

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2:

    def zigzagLevelOrder(self, a1):
        if not a1:
            return []
        v1 = []
        v2 = [a1]
        v3 = True
        while v2:
            v4 = []
            v5 = []
            for v6 in v2:
                v4.append(v6.val)
                if v3:
                    if v6.left:
                        v5.append(v6.left)
                    if v6.right:
                        v5.append(v6.right)
                else:
                    if v6.right:
                        v5.append(v6.right)
                    if v6.left:
                        v5.append(v6.left)
            v1.append(v4)
            v2 = v5
            v3 = not v3
        return v1
