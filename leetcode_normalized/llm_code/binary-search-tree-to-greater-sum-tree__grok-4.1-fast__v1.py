class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def bstToGst(self, a1):
        v1 = []
        v2 = a1
        v3 = 0
        while v2 or v1:
            while v2:
                v1.append(v2)
                v2 = v2.right
            v2 = v1.pop()
            v2.val += v3
            v3 = v2.val
            v2 = v2.left
        return a1
