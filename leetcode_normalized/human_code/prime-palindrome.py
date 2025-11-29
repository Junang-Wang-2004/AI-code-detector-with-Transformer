class C1(object):

    def primePalindrome(self, a1):
        """
        """

        def is_prime(a1):
            if a1 < 2 or a1 % 2 == 0:
                return a1 == 2
            return all((a1 % d for v1 in range(3, int(a1 ** 0.5) + 1, 2)))
        if 8 <= a1 <= 11:
            return 11
        for v1 in range(10 ** (len(str(a1)) // 2), 10 ** 5):
            v2 = int(str(v1) + str(v1)[-2::-1])
            if v2 >= a1 and is_prime(v2):
                return v2
