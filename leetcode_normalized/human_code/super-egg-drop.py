class C1(object):

    def superEggDrop(self, a1, a2):
        """
        """

        def check(a1, a2, a3):
            v1, v2 = (0, 1)
            for v3 in range(1, a2 + 1):
                v2 *= a1 - v3 + 1
                v2 //= v3
                v1 += v2
                if v1 >= a3:
                    return True
            return False
        v1, v2 = (1, a2)
        while v1 <= v2:
            v3 = v1 + (v2 - v1) // 2
            if check(v3, a1, a2):
                v2 = v3 - 1
            else:
                v1 = v3 + 1
        return v1
