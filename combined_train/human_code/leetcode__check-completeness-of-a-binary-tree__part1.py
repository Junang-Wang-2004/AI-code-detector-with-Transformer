class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def isCompleteTree(self, a1):
        """
        """
        v1 = False
        v2 = [a1]
        while v2:
            v3 = []
            for v4 in v2:
                if not v4:
                    v1 = True
                    continue
                if v1:
                    return False
                v3.append(v4.left)
                v3.append(v4.right)
            v2 = v3
        return True
