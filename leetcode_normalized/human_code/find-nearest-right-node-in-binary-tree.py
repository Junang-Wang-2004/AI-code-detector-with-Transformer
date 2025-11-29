class C1(object):

    def __init__(self, a1=0, a2=None, a3=None):
        pass

class C2(object):

    def findNeartestRightNode(self, a1, a2):
        """
        """
        v1 = [a1]
        while v1:
            v2 = []
            for v3, v4 in enumerate(v1):
                if v4 == a2:
                    return v1[v3 + 1] if v3 + 1 < len(v1) else None
                if v4.left:
                    v2.append(v4.left)
                if v4.right:
                    v2.append(v4.right)
            v1 = v2
        return None
