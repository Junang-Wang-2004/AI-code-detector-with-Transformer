class C1(object):

    def findMaximumNumber(self, a1, a2):
        """
        """

        def binary_search_right(a1, a2, a3):
            while a1 <= a2:
                v1 = a1 + (a2 - a1) // 2
                if not a3(v1):
                    a2 = v1 - 1
                else:
                    a1 = v1 + 1
            return a2

        def count(a1):
            v1 = v2 = 0
            while 1 << v2 + a2 - 1 <= a1:
                v3, v4 = divmod(a1 + 1, 1 << v2 + a2 - 1 + 1)
                v1 += v3 * 1 * (1 << v2 + a2 - 1) + max(v4 - 1 * (1 << v2 + a2 - 1), 0)
                v2 += a2
            return v1
        return binary_search_right(1, max(a1 << 2, 1 << a2), lambda v: count(v) <= a1)
