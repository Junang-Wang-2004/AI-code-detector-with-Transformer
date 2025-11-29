# Time:  O(n)
# Space: O(1)

# greedy
class Solution(object):
    def maxSumOfSquares(self, num, sum):
        """
        """
        if num*9 < sum:
            return ""
        q, r = divmod(sum, 9)
        result = ['0']*num
        for i in range(q):
            result[i] = '9'
        if r:
            result[q] = str(r)
        return "".join(result)
