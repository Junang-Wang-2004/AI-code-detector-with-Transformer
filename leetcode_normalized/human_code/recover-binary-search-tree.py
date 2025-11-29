class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

    def __repr__(self):
        if self:
            v1 = []
            v2 = [self]
            while v2:
                v3 = v2[0]
                if v3:
                    v1.append(v3.val)
                    v2.append(v3.left)
                    v2.append(v3.right)
                else:
                    v1.append('#')
                v2 = v2[1:]
            while v1[-1] == '#':
                v1.pop()
            return repr(v1)
        else:
            return None

class C2(object):

    def recoverTree(self, a1):
        return self.MorrisTraversal(a1)

    def MorrisTraversal(self, a1):
        if a1 is None:
            return
        v1 = [None, None]
        v2, v3 = (None, a1)
        while v3:
            if v3.left is None:
                self.detectBroken(v1, v2, v3)
                v2 = v3
                v3 = v3.right
            else:
                v4 = v3.left
                while v4.right and v4.right != v3:
                    v4 = v4.right
                if v4.right is None:
                    v4.right = v3
                    v3 = v3.left
                else:
                    self.detectBroken(v1, v2, v3)
                    v4.right = None
                    v2 = v3
                    v3 = v3.right
        v1[0].val, v1[1].val = (v1[1].val, v1[0].val)
        return a1

    def detectBroken(self, a1, a2, a3):
        if a2 and a2.val > a3.val:
            if a1[0] is None:
                a1[0] = a2
            a1[1] = a3
