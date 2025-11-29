class C1(object):

    def __init__(self, a1=0, a2=None, a3=None):
        pass

class C2(object):

    def minimumLevel(self, a1):
        """
        """
        v1 = [a1]
        v2 = 1
        v3 = (float('inf'), float('inf'))
        while v1:
            v4 = []
            v5 = 0
            for v6 in v1:
                if v6.left:
                    v4.append(v6.left)
                if v6.right:
                    v4.append(v6.right)
                v5 += v6.val
            v3 = min(v3, (v5, v2))
            v1 = v4
            v2 += 1
        return v3[-1]
