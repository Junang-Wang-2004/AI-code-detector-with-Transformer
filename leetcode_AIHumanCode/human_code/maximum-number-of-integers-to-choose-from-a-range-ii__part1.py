# Time:  O(b)
# Space: O(b)

# math
class Solution(object):
    def maxCount(self, banned, n, maxSum):
        """
        """
        k = min(int((-1+(1+8*maxSum))**0.5/2), n)  # k = argmax((k+1)*k//2 <= maxSum)
        total = (k+1)*k//2
        result = k
        lookup = set(banned)
        for x in lookup:
            if x <= k:
                total -= x
                result -= 1
        for i in range(k+1, n+1):
            if i in lookup:
                continue
            if total+i > maxSum:
                break
            total += i
            result += 1
        return result


