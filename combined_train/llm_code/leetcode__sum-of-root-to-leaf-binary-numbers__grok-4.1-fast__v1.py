class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def sumRootToLeaf(self, a1):
        v1 = 10 ** 9 + 7
        if not a1:
            return 0
        v2 = 0
        v3 = [(a1, 0)]
        while v3:
            v4, v5 = v3.pop()
            v5 = ((v5 << 1) + v4.val) % v1
            if not v4.left and (not v4.right):
                v2 = (v2 + v5) % v1
            else:
                if v4.right:
                    v3.append((v4.right, v5))
                if v4.left:
                    v3.append((v4.left, v5))
        return v2
