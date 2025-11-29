from functools import reduce

class C1(object):

    def largestPalindrome(self, a1, a2):
        """
        """

        def inv(a1, a2):
            return pow(a1, a2 - 2, a2)

        def f(a1):
            v1 = 7
            v2 = ['9'] * a1
            if a1:
                v3 = reduce(lambda accu, x: (accu * 10 + (ord(x) - ord('0'))) % v1, v2, 0)
                v4 = 9 - v3 * inv(11 if a1 % 2 == 0 else 1, v1) * inv(pow(10, a1 // 2 - int(a1 % 2 == 0), v1), v1) % v1
                if v4 <= 2:
                    v4 += v1
                v2[a1 // 2] = v2[a1 // 2 - int(a1 % 2 == 0)] = str(v4)
            return ''.join(v2)
        if a2 in (1, 3, 9):
            return '9' * a1
        if a2 in (2, 4, 8):
            a2 = min(a2, 6)
            if a1 <= a2:
                return '8' * a1
            v2 = a2 // 2
            return '8' * v2 + '9' * (a1 - a2) + '8' * v2
        if a2 == 5:
            if a1 <= 2:
                return '5' * a1
            return '5' + '9' * (a1 - 2) + '5'
        if a2 == 6:
            if a1 <= 2:
                return '6' * a1
            if a1 % 2:
                v2 = a1 // 2 - 1
                return '8' + '9' * v2 + '8' + '9' * v2 + '8'
            v2 = a1 // 2 - 2
            return '8' + '9' * v2 + '77' + '9' * v2 + '8'
        v2, v3 = divmod(a1, 12)
        return '999999' * v2 + f(v3) + '999999' * v2
