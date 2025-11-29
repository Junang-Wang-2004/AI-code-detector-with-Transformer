class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def pathSum(self, a1, a2):
        return self.pathSumRecu([], [], a1, a2)

    def pathSumRecu(self, a1, a2, a3, a4):
        if a3 is None:
            return a1
        if a3.left is None and a3.right is None and (a3.val == a4):
            a1.append(a2 + [a3.val])
            return a1
        a2.append(a3.val)
        self.pathSumRecu(a1, a2, a3.left, a4 - a3.val)
        self.pathSumRecu(a1, a2, a3.right, a4 - a3.val)
        a2.pop()
        return a1
