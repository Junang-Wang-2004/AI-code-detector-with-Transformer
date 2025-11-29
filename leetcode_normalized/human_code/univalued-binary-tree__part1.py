class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def isUnivalTree(self, a1):
        """
        """
        v1 = [a1]
        while v1:
            v2 = v1.pop()
            if not v2:
                continue
            if v2.val != a1.val:
                return False
            v1.append(v2.left)
            v1.append(v2.right)
        return True
