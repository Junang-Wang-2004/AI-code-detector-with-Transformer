# Time:  O(n)
# Space: O(1)
class Solution3(object):
    def numberOfSubstrings(self, s):
        """
        """
        result, right, count = 0, 0, [0]*3
        for left, c in enumerate(s):
            while right < len(s) and not all(count):
                count[ord(s[right])-ord('a')] += 1
                right += 1
            if all(count):
                result += (len(s)-1) - (right-1) + 1
            count[ord(c)-ord('a')] -= 1
        return result
