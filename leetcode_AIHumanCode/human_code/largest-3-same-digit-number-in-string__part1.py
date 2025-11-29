# Time:  O(n)
# Space: O(1)

# string
class Solution(object):
    def largestGoodInteger(self, num):
        """
        """
        result = ''
        cnt = 0
        for i, x in enumerate(num):
            cnt += 1
            if i+1 < len(num) and num[i] == num[i+1]:
                continue
            if cnt >= 3:
                result = max(result, num[i])
            cnt = 0
        return result*3


