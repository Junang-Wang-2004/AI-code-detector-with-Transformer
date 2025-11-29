class Solution(object):
    def minimizeXor(self, num1, num2):
        target = 0
        temp = num2
        while temp:
            target += temp & 1
            temp >>= 1
        result = 0
        placed = 0
        for pos in range(60, -1, -1):
            pref = (num1 >> pos) & 1
            rem_need = target - placed - pref
            rem_pos = pos
            if 0 <= rem_need <= rem_pos:
                bit = pref
            else:
                bit = 1 ^ pref
            result |= bit << pos
            placed += bit
        return result
