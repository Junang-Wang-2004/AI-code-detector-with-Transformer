# Time:  O(n + r)
# Space: O(r)

# if r is small, this is better
class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        """
        RANGE_SIZE = 50

        interval = [0]*(RANGE_SIZE+1)
        for l, r in ranges:
            interval[l-1] += 1
            interval[(r-1)+1] -= 1
        cnt = 0
        for i in range((right-1)+1):
            cnt += interval[i]
            if i >= left-1 and not cnt:
                return False
        return True


