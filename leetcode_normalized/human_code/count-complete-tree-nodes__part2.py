class C1(object):

    def countNodes(self, a1):
        """
        """

        def check(a1, a2):
            v1 = 1
            while v1 <= a2:
                v1 <<= 1
            v1 >>= 2
            while v1:
                if a2 & v1 == 0:
                    a1 = a1.left
                else:
                    a1 = a1.right
                v1 >>= 1
            return bool(a1)
        if not a1:
            return 0
        v1, v2 = (a1, 0)
        while v1.left:
            v1 = v1.left
            v2 += 1
        v3, v4 = (2 ** v2, 2 ** (v2 + 1) - 1)
        while v3 <= v4:
            v5 = v3 + (v4 - v3) // 2
            if not check(a1, v5):
                v4 = v5 - 1
            else:
                v3 = v5 + 1
        return v4
