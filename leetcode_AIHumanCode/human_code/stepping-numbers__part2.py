# Time:  O(k + r), r is the size of result
# Space: O(k), k is the size of stepping numbers in [0, high]
class Solution2(object):
    def countSteppingNumbers(self, low, high):
        """
        """
        result = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(1, high):
            if result[-1] >= high:
                break
            d1 = result[i]%10 - 1
            if d1 >= 0:
                result.append(result[i]*10 + d1)
            d2 = result[i]%10 + 1
            if d2 <= 9:
                result.append(result[i]*10 + d2)
        result.append(float("inf"))
        lit = bisect.bisect_left(result, low)
        rit = bisect.bisect_right(result, high)
        return result[lit:rit]
