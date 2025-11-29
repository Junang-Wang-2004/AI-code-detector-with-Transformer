class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def sumNumbers(self, a1):
        if not a1:
            return 0
        v1 = [(a1, a1.val)]
        v2 = 0
        while v1:
            v3, v4 = v1.pop()
            if not v3.left and (not v3.right):
                v2 += v4
                continue
            if v3.right:
                v1.append((v3.right, v4 * 10 + v3.right.val))
            if v3.left:
                v1.append((v3.left, v4 * 10 + v3.left.val))
        return v2
