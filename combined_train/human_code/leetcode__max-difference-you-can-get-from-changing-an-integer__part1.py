class C1(object):

    def maxDiff(self, a1):
        """
        """

        def find(a1, a2):
            v1 = 0
            while a1:
                a1, v3 = divmod(a1, 10)
                if a2(v3):
                    v1 = v3
            return v1

        def reverse(a1, a2):
            v1 = 0
            while a1 or a2 > 0:
                a1, v3 = divmod(a1, 10)
                v1 = v1 * 10 + v3
                a2 -= 1
            return v1

        def replace(a1, a2, a3):
            v1 = v2 = 0
            while a1:
                a1, v4 = divmod(a1, 10)
                if v4 == a2:
                    v4 = a3
                v1 = v1 * 10 + v4
                v2 += 1
            return reverse(v1, v2)
        v1 = find(a1, lambda x: x < 9)
        v2 = find(a1, lambda x: x > 1)
        return replace(a1, v1, 9) - replace(a1, v2, 1 if reverse(a1, 0) % 10 != 1 else 0)
