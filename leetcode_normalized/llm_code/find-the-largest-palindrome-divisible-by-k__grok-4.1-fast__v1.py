class C1(object):

    def largestPalindrome(self, a1, a2):
        if a2 in (1, 3, 9):
            return '9' * a1
        elif a2 == 5:
            if a1 <= 2:
                return '5' * a1
            return '5' + '9' * (a1 - 2) + '5'
        elif a2 == 6:
            if a1 <= 2:
                return '6' * a1
            if a1 % 2:
                v1 = a1 // 2 - 1
                return '8' + '9' * v1 + '8' + '9' * v1 + '8'
            v1 = a1 // 2 - 2
            return '8' + '9' * v1 + '77' + '9' * v1 + '8'
        elif a2 in (2, 4, 8):
            v2 = {2: 1, 4: 2, 8: 3}[a2]
            v3 = 2 * v2
            if a1 <= v3:
                return '8' * a1
            return '8' * v2 + '9' * (a1 - v3) + '8' * v2
        else:
            v4 = 6
            v5 = a1 // (2 * v4)
            v6 = a1 % (2 * v4)
            v7 = '999999' * v5
            v8 = self._build_mod7_pal(v6)
            return v7 + v8 + v7

    def _build_mod7_pal(self, a1):
        if a1 == 0:
            return ''
        v1 = ['9'] * a1
        v2 = a1 // 2
        for v3 in range(9, -1, -1):
            v4 = v1[:]
            v4[v2] = chr(48 + v3)
            if a1 % 2 == 0:
                v4[v2 - 1] = chr(48 + v3)
            v5 = 0
            for v6 in v4:
                v5 = (v5 * 10 + (ord(v6) - 48)) % 7
            if v5 == 0:
                return ''.join(v4)
        return ''
