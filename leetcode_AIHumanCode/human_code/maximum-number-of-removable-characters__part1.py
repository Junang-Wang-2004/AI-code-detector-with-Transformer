# Time:  O(rlogn)
# Space: O(r)

# if r = O(1), this is better
class Solution(object):
    def maximumRemovals(self, s, p, removable):
        """
        """
        def check(s, p, removable, x):
            lookup = set(removable[i] for i in range(x))
            j = 0
            for i in range(len(s)):
                if i in lookup or s[i] != p[j]:
                    continue
                j += 1
                if j == len(p):
                    return True
            return False

        left, right = 0, len(removable)
        while left <= right:
            mid = left + (right-left)//2
            if not check(s, p, removable, mid):
                right = mid-1
            else:
                left = mid+1
        return right


