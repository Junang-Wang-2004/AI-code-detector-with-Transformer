# Time:  O(31)
# Space: O(1)

class Solution(object):
    def minFlips(self, a, b, c):
        """
        """
        def number_of_1_bits(n):
            result = 0
            while n:
                n &= n-1
                result += 1
            return result

        return number_of_1_bits((a|b)^c) + number_of_1_bits(a&b&~c)


