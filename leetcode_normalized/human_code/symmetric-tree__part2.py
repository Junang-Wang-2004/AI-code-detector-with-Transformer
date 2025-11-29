class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def isSymmetric(self, a1):
        if a1 is None:
            return True
        return self.isSymmetricRecu(a1.left, a1.right)

    def isSymmetricRecu(self, a1, a2):
        if a1 is None and a2 is None:
            return True
        if a1 is None or a2 is None or a1.val != a2.val:
            return False
        return self.isSymmetricRecu(a1.left, a2.right) and self.isSymmetricRecu(a1.right, a2.left)
