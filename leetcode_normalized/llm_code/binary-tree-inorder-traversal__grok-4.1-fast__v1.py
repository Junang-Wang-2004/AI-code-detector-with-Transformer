class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def inorderTraversal(self, a1):
        v1 = []
        v2 = []
        v3 = a1
        while v2 or v3:
            while v3:
                v2.append(v3)
                v3 = v3.left
            v3 = v2.pop()
            v1.append(v3.val)
            v3 = v3.right
        return v1
