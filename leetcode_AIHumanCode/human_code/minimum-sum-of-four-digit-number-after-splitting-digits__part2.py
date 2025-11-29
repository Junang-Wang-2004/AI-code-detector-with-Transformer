# Time:  O(dlogd) = O(1), d is the number of digits
# Space: O(d) = O(1)
# greedy
class Solution2(object):
    def minimumSum(self, num):
        """
        """
        nums = sorted(map(int, list(str(num))))
        a = b = 0
        for x in nums:
            a = a*10+x
            a, b = b, a
        return a+b
