class Solution:
    def countPrimeSetBits(self, left, right):
        valid_counts = {2, 3, 5, 7, 11, 13, 17, 19}
        cnt = 0
        for val in range(left, right + 1):
            ones = bin(val).count('1')
            if ones in valid_counts:
                cnt += 1
        return cnt
