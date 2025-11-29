class C1(object):

    def __init__(self, a1=0, a2=None, a3=None):
        pass

class C2(object):

    def reverseOddLevels(self, a1):
        """
        """
        v1 = [a1]
        v2 = 0
        while v1:
            if v2:
                v3, v4 = (0, len(v1) - 1)
                while v3 < v4:
                    v1[v3].val, v1[v4].val = (v1[v4].val, v1[v3].val)
                    v3 += 1
                    v4 -= 1
            if not v1[0].left:
                break
            v5 = []
            for v6 in v1:
                v5.append(v6.left)
                v5.append(v6.right)
            v1 = v5
            v2 ^= 1
        return a1
