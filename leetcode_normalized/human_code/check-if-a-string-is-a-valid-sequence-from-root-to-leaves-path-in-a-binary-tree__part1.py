class C1(object):

    def __init__(self, a1=0, a2=None, a3=None):
        self.val = a1
        self.left = a2
        self.right = a3

class C2(object):

    def isValidSequence(self, a1, a2):
        """
        """
        v1 = [a1]
        for v2 in range(len(a2)):
            v3 = []
            while v1:
                v4 = v1.pop()
                if not v4 or v4.val != a2[v2]:
                    continue
                if v2 + 1 == len(a2) and v4.left == v4.right:
                    return True
                v3.extend((child for v5 in (v4.left, v4.right)))
            v1 = v3
        return False
