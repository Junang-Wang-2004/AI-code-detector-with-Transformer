# Time:  O(n + 26^3 * logn)
# Space: O(n)
import bisect


# hash table, binary search
class Solution2(object):
    def maxSubstringLength(self, s):
        """
        """
        def check(left, right):
            for x in idxs:
                if not x:
                    continue
                l = bisect.bisect_left(x, left)
                r = bisect.bisect_right(x, right)-1
                if not (r-l+1 == len(x) or r-l+1 == 0):
                    return False
            return True

        idxs = [[] for _ in range(26)]
        for i, x in enumerate(s):
            idxs[ord(x)-ord('a')].append(i)
        result = -1
        for x in idxs:
            if not x:
                continue
            left = x[0]
            for y in idxs:
                if not y:
                    continue
                right = y[-1]
                if left <= right and right-left+1 != len(s) and check(left, right):
                    result = max(result, right-left+1)
        return result


