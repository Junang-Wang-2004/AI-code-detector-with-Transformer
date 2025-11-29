class C1(object):

    def __init__(self, a1=0, a2=None, a3=None):
        self.val = a1
        self.left = a2
        self.right = a3

class C2(object):

    def pseudoPalindromicPaths(self, a1):
        """
        """
        v1 = 0
        v2 = [(a1, 0)]
        while v2:
            v3, v4 = v2.pop()
            if not v3:
                continue
            v4 ^= 1 << v3.val - 1
            v1 += int(v3.left == v3.right and v4 & v4 - 1 == 0)
            v2.append((v3.right, v4))
            v2.append((v3.left, v4))
        return v1
