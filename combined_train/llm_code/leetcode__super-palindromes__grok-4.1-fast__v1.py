class C1(object):

    def superpalindromesInRange(self, a1, a2):

        def is_palindrome(a1):
            v1 = str(a1)
            return v1 == v1[::-1]
        v1 = int(a1)
        v2 = int(a2)
        v3 = int(v2 ** 0.25) + 1
        v4 = 0
        for v5 in range(1, v3 + 1):
            v6 = str(v5)
            v7 = int(v6 + v6[:-1][::-1])
            v8 = v7 * v7
            if v1 <= v8 <= v2 and is_palindrome(v8):
                v4 += 1
            v9 = int(v6 + v6[::-1])
            v10 = v9 * v9
            if v1 <= v10 <= v2 and is_palindrome(v10):
                v4 += 1
        return v4
