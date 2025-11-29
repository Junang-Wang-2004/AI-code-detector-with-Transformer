class C1:

    def __init__(self, a1=0, a2=None, a3=None):
        self.val = a1
        self.left = a2
        self.right = a3

class C2:

    def levelOrder(self, a1):
        if not a1:
            return []
        v1 = []
        v2 = [a1]
        v3 = 0
        while v3 < len(v2):
            v4 = len(v2) - v3
            v5 = []
            for v6 in range(v4):
                v7 = v2[v3]
                v5.append(v7.val)
                if v7.left:
                    v2.append(v7.left)
                if v7.right:
                    v2.append(v7.right)
                v3 += 1
            v1.append(v5)
        return v1
