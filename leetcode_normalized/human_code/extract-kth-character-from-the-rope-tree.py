class C1(object):

    def __init__(self, a1=0, a2='', a3=None, a4=None):
        pass

class C2(object):

    def getKthCharacter(self, a1, a2):
        """
        """
        while a1.len:
            v1 = max(a1.left.len, len(a1.left.val)) if a1.left else 0
            if a2 <= v1:
                a1 = a1.left
            else:
                a2 -= v1
                a1 = a1.right
        return a1.val[a2 - 1]
