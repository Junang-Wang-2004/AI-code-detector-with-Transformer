# Time:  O(sqrt(n))
# Space: O(1)
class Solution2(object):
    def closestDivisors(self, num):
        """
        """
        result, d = [1, num+1], 1
        while d*d <= num+2:
            if (num+2) % d == 0:
                result = [d, (num+2)//d]
            if (num+1) % d == 0:
                result = [d, (num+1)//d]
            d += 1
        return result
