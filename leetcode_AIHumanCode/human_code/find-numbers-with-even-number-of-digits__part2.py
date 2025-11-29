# Time:  O(nlogm), n the length of nums, m is the max value of nums
# Space: O(logm)
class Solution2(object):
    def findNumbers(self, nums):
        """
        """
        def digit_count(n):
            result = 0
            while n:
                n //= 10
                result += 1
            return result

        return sum(digit_count(n) % 2 == 0 for n in nums)


