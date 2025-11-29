class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def constructFromPrePost(self, a1, a2):
        """
        """
        v1 = [C1(a1[0])]
        v2 = 0
        for v3 in range(1, len(a1)):
            v4 = C1(a1[v3])
            while v1[-1].val == a2[v2]:
                v1.pop()
                v2 += 1
            if not v1[-1].left:
                v1[-1].left = v4
            else:
                v1[-1].right = v4
            v1.append(v4)
        return v1[0]
