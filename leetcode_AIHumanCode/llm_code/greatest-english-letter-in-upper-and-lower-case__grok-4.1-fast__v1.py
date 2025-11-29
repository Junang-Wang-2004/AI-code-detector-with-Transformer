class Solution:
    def greatestLetter(self, s):
        low_mask = 0
        up_mask = 0
        for char in s:
            o = ord(char)
            if ord('a') <= o <= ord('z'):
                low_mask |= 1 << (o - ord('a'))
            elif ord('A') <= o <= ord('Z'):
                up_mask |= 1 << (o - ord('A'))
        for i in range(25, -1, -1):
            if (up_mask & (1 << i)) != 0 and (low_mask & (1 << i)) != 0:
                return chr(ord('A') + i)
        return ""
