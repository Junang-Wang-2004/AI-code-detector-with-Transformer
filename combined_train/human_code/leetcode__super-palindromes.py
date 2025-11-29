class C1(object):

    def superpalindromesInRange(self, a1, a2):
        """
        """

        def is_palindrome(a1):
            return str(a1) == str(a1)[::-1]
        v1 = int(10 ** ((len(a2) + 1) * 0.25))
        v2, v3 = (int(a1), int(a2))
        v4 = 0
        for v5 in range(v1):
            v6 = str(v5)
            v7 = v6 + v6[-2::-1]
            v8 = int(v7) ** 2
            if v8 > v3:
                break
            if v8 >= v2 and is_palindrome(v8):
                v4 += 1
        for v5 in range(v1):
            v6 = str(v5)
            v7 = v6 + v6[::-1]
            v8 = int(v7) ** 2
            if v8 > v3:
                break
            if v8 >= v2 and is_palindrome(v8):
                v4 += 1
        return v4
