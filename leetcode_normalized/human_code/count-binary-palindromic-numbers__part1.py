class C1(object):

    def countBinaryPalindromes(self, a1):
        """
        """

        def length(a1):
            v1 = 0
            while a1:
                v1 += 1
                a1 >>= 1
            return v1

        def reverse(a1, a2):
            v1 = 0
            for v2 in range(a2):
                if a1 & 1 << v2:
                    v1 |= 1 << a2 - 1 - v2
            return v1
        v1 = length(a1) // 2
        return (1 << v1) - 1 + (a1 >> v1) + int(a1 >> v1 << v1 | reverse(a1 >> length(a1) - v1, v1) <= a1)
