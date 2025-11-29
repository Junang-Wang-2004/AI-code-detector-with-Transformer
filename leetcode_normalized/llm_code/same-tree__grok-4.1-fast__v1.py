class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def isSameTree(self, a1, a2):
        v1 = [(a1, a2)]
        while v1:
            v2, v3 = v1.pop()
            if v2 is None and v3 is None:
                continue
            if v2 is None or v3 is None or v2.val != v3.val:
                return False
            v1.append((v2.right, v3.right))
            v1.append((v2.left, v3.left))
        return True
