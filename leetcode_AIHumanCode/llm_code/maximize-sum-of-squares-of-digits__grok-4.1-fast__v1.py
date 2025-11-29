class Solution(object):
    def maxSumOfSquares(self, num, total):
        if total > 9 * num:
            return ""
        full_nines = total // 9
        rem = total % 9
        trailing_zeros = num - full_nines - (1 if rem > 0 else 0)
        front = '9' * full_nines
        middle = str(rem) if rem > 0 else ''
        back = '0' * trailing_zeros
        return front + middle + back
