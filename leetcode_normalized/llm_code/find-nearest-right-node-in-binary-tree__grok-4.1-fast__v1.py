class C1(object):

    def __init__(self, a1=0, a2=None, a3=None):
        self.val = a1
        self.left = a2
        self.right = a3

class C2(object):

    def findNeartestRightNode(self, a1, a2):
        if not a1:
            return None
        v1 = [a1]
        while v1:
            v2 = len(v1)
            v3 = v2
            for v4 in range(v2):
                v5 = v1.pop(0)
                v3 -= 1
                if v5 == a2:
                    return v1[0] if v3 > 0 else None
                if v5.left:
                    v1.append(v5.left)
                if v5.right:
                    v1.append(v5.right)
        return None
