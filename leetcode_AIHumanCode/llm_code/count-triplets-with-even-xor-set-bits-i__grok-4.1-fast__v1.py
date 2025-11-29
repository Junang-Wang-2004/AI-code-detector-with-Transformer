class Solution:
    def tripletCount(self, a, b, c):
        def bit_parity(n):
            parity = 0
            while n:
                parity ^= n & 1
                n >>= 1
            return parity
        
        def parity_counts(nums):
            even = 0
            for num in nums:
                if bit_parity(num) == 0:
                    even += 1
            return even, len(nums) - even
        
        even_a, odd_a = parity_counts(a)
        even_b, odd_b = parity_counts(b)
        even_c, odd_c = parity_counts(c)
        
        return (even_a * even_b * even_c +
                odd_a * odd_b * even_c +
                odd_a * even_b * odd_c +
                even_a * odd_b * odd_c)
