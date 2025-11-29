# Time:  O(26^2 * n)
# Space: O(26)
# hash table, brute force
class Solution5(object):
    def maxSubstringLength(self, s):
        """
        """
        def check(l, r):
            return all(l <= left[ord(s[i])-ord('a')] and right[ord(s[i])-ord('a')] <= r for i in range(l, r+1))

        left, right = [-1]*26, [-1]*26
        for i, x in enumerate(s):
            x = ord(x)-ord('a')
            if left[x] == -1:
                left[x] = i
            right[x] = i
        result = -1
        for l in left:
            if l == -1:
                continue
            for r in right:
                if r == -1:
                    continue
                if l <= r and result < r-l+1 != len(s) and check(l, r):
                    result = r-l+1
        return result
