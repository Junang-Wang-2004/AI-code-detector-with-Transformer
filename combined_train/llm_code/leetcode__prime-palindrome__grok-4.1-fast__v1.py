class C1:

    def primePalindrome(self, a1):
        v1 = [2, 3, 5, 7, 11]
        for v2 in v1:
            if v2 >= a1:
                return v2

        def is_prime(a1):
            if a1 <= 1:
                return False
            if a1 <= 3:
                return True
            if a1 % 2 == 0 or a1 % 3 == 0:
                return False
            v1 = 5
            while v1 * v1 <= a1:
                if a1 % v1 == 0 or a1 % (v1 + 2) == 0:
                    return False
                v1 += 6
            return True
        v3 = len(str(a1))
        v4 = 10 ** (v3 // 2)
        for v5 in range(v4, 10 ** 5 + 1):
            v6 = str(v5)
            v7 = v6[:-1][::-1]
            v8 = int(v6 + v7)
            if v8 >= a1 and is_prime(v8):
                return v8
