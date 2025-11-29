class C1(object):

    def __init__(self, a1=0, a2=None, a3=None):
        self.val = a1
        self.left = a2
        self.right = a3

class C2(object):

    def isEvenOddTree(self, a1):
        v1 = [a1] if a1 else []
        v2 = 0
        while v1:
            v3 = []
            v4 = []
            for v5 in v1:
                v4.append(v5.val)
                if v5.left:
                    v3.append(v5.left)
                if v5.right:
                    v3.append(v5.right)
            for v6 in range(len(v4)):
                v7 = v4[v6]
                if v2 % 2 == 0:
                    if v7 % 2 == 0 or (v6 > 0 and v4[v6 - 1] >= v7):
                        return False
                elif v7 % 2 != 0 or (v6 > 0 and v4[v6 - 1] <= v7):
                    return False
            v1 = v3
            v2 += 1
        return True
