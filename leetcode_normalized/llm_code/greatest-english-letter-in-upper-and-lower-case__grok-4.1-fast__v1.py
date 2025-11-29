class C1:

    def greatestLetter(self, a1):
        v1 = 0
        v2 = 0
        for v3 in a1:
            v4 = ord(v3)
            if ord('a') <= v4 <= ord('z'):
                v1 |= 1 << v4 - ord('a')
            elif ord('A') <= v4 <= ord('Z'):
                v2 |= 1 << v4 - ord('A')
        for v5 in range(25, -1, -1):
            if v2 & 1 << v5 != 0 and v1 & 1 << v5 != 0:
                return chr(ord('A') + v5)
        return ''
