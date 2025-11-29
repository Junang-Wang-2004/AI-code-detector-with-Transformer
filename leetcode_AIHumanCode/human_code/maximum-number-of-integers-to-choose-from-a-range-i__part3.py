# Time:  O(n)
# Space: O(b)
# greedy
class Solution3(object):
    def maxCount(self, banned, n, maxSum):
        """
        """
        lookup = set(banned)
        result = total = 0
        for i in range(1, n+1):
            if i in lookup:
                continue
            if total+i > maxSum:
                break
            total += i
            result += 1
        return result
