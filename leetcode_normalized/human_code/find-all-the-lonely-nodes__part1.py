class C1(object):

    def __init__(self, a1=0, a2=None, a3=None):
        self.val = a1
        self.left = a2
        self.right = a3

class C2(object):

    def getLonelyNodes(self, a1):
        """
        """
        v1 = []
        v2 = [a1]
        while v2:
            v3 = v2.pop()
            if not v3:
                continue
            if v3.left and (not v3.right):
                v1.append(v3.left.val)
            elif v3.right and (not v3.left):
                v1.append(v3.right.val)
            v2.append(v3.right)
            v2.append(v3.left)
        return v1
