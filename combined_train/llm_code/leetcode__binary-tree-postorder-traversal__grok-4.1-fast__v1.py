class C1:

    def __init__(self, a1):
        self.val = a1
        self.left = self.right = None

class C2:

    def postorderTraversal(self, a1):
        if not a1:
            return []
        v1, v2 = ([a1], [])
        while v1:
            v3 = v1.pop()
            v2.append(v3)
            if v3.right:
                v1.append(v3.right)
            if v3.left:
                v1.append(v3.left)
        v4 = []
        while v2:
            v4.append(v2.pop().val)
        return v4
