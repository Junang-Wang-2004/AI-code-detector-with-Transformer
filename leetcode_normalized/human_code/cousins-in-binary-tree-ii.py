class C1(object):

    def __init__(self, a1=0, a2=None, a3=None):
        pass

class C2(object):

    def replaceValueInTree(self, a1):
        """
        """
        v1 = [(a1, a1.val)]
        while v1:
            v2 = []
            v3 = sum((node.val for v4, v5 in v1))
            for v4, v6 in v1:
                v4.val = v3 - v6
                v6 = (v4.left.val if v4.left else 0) + (v4.right.val if v4.right else 0)
                if v4.left:
                    v2.append((v4.left, v6))
                if v4.right:
                    v2.append((v4.right, v6))
            v1 = v2
        return a1
