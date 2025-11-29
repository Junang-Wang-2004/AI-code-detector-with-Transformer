class C1(object):

    def __init__(self, a1=0, a2=None, a3=None):
        pass

class C2(object):

    def heightOfTree(self, a1):
        """
        """
        v1 = -1
        v2 = [(a1, 0)]
        while v2:
            v3, v4 = v2.pop()
            v1 = max(v1, v4)
            if v3.right and v3.right.left != v3:
                v2.append((v3.right, v4 + 1))
            if v3.left and v3.left.right != v3:
                v2.append((v3.left, v4 + 1))
        return v1
