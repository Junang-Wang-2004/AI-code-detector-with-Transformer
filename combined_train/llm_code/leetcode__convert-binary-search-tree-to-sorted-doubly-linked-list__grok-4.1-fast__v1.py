class C1(object):

    def __init__(self, a1, a2, a3):
        self.val = a1
        self.left = a2
        self.right = a3

class C2(object):

    def treeToDoublyList(self, a1):
        if not a1:
            return None
        v1 = []
        v2 = None
        v3 = None
        v4 = a1
        while v4 or v1:
            while v4:
                v1.append(v4)
                v4 = v4.left
            v4 = v1.pop()
            v4.left = v2
            if v2:
                v2.right = v4
            else:
                v3 = v4
            v2 = v4
            v4 = v4.right
        v2.right = v3
        v3.left = v2
        return v3
