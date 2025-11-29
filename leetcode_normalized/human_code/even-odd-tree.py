class C1(object):

    def __init__(self, a1=0, a2=None, a3=None):
        self.val = a1
        self.left = a2
        self.right = a3

class C2(object):

    def isEvenOddTree(self, a1):
        """
        """
        v1 = [a1]
        v2 = False
        while v1:
            v3 = []
            v4 = None
            for v5 in v1:
                if v2:
                    if v5.val % 2 or (v4 and v4.val <= v5.val):
                        return False
                elif not v5.val % 2 or (v4 and v4.val >= v5.val):
                    return False
                if v5.left:
                    v3.append(v5.left)
                if v5.right:
                    v3.append(v5.right)
                v4 = v5
            v1 = v3
            v2 = not v2
        return True
