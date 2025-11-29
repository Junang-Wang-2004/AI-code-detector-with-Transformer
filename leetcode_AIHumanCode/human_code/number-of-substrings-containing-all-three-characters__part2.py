# Time:  O(n)
# Space: O(1)
class Solution2(object):
    def numberOfSubstrings(self, s):
        """
        """
        result, left, count = 0, 0, [0]*3
        for right, c in enumerate(s):
            count[ord(s[right])-ord('a')] += 1
            while all(count):
                count[ord(s[left])-ord('a')] -= 1
                left += 1
            result += left
        return result


