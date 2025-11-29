class C1(object):

    def countGoodIntegers(self, a1, a2):
        """
        """

        def reverse(a1, a2):
            if a2 % 2:
                a1 //= 10
            v2 = 0
            while a1:
                v2 = v2 * 10 + a1 % 10
                a1 //= 10
            return v2

        def palindrome(a1, a2):
            return a1 * 10 ** (a2 // 2) + reverse(a1, a2)

        def count(a1):
            v1 = [0] * 10
            while a1:
                v1[a1 % 10] += 1
                a1 //= 10
            return tuple(v1)
        v1 = [1] * (a1 + 1)
        for v2 in range(len(v1) - 1):
            v1[v2 + 1] = v1[v2] * (v2 + 1)
        v3 = (a1 + 1) // 2
        v4 = 0
        v5 = set()
        for v6 in range(10 ** (v3 - 1), 10 ** v3):
            v7 = palindrome(v6, a1)
            if v7 % a2:
                continue
            v8 = count(v7)
            if v8 in v5:
                continue
            v5.add(v8)
            v9 = (a1 - v8[0]) * v1[a1 - 1]
            for v10 in v8:
                v9 //= v1[v10]
            v4 += v9
        return v4
