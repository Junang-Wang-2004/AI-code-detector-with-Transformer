class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def recoverFromPreorder(self, a1):
        """
        """
        v1 = 0
        v2 = []
        while v1 < len(a1):
            v3 = 0
            while v1 < len(a1) and a1[v1] == '-':
                v3 += 1
                v1 += 1
            while len(v2) > v3:
                v2.pop()
            v4 = []
            while v1 < len(a1) and a1[v1] != '-':
                v4.append(a1[v1])
                v1 += 1
            v5 = C1(int(''.join(v4)))
            if v2:
                if v2[-1].left is None:
                    v2[-1].left = v5
                else:
                    v2[-1].right = v5
            v2.append(v5)
        return v2[0]
