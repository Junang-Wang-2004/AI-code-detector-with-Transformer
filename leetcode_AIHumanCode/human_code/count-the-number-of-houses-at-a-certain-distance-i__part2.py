# Time:  O(n^2)
# Space: O(1)
# math
class Solution2(object):
    def countOfPairs(self, n, x, y):
        """
        """
        x, y = x-1, y-1
        result = [0]*n
        for i in range(n):
            for j in range(i+1, n):
                result[min(abs(i-j), abs(i-x)+1+abs(y-j), abs(i-y)+1+abs(x-j))-1] += 2
        return result
