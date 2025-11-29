class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def isSymmetric(self, a1):
        if a1 is None:
            return True
        v1 = []
        v1.append(a1.left)
        v1.append(a1.right)
        while v1:
            v2, v3 = (v1.pop(), v1.pop())
            if v2 is None and v3 is None:
                continue
            if v2 is None or v3 is None or v2.val != v3.val:
                return False
            v1.append(v2.left)
            v1.append(v3.right)
            v1.append(v2.right)
            v1.append(v3.left)
        return True
