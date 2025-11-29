# Time:  O(26 + n^2)
# Space: O(26 + n^2)
# string, brute force, freq table
class Solution2(object):
    def maximumLength(self, s):
        """
        """
        lookup = [[0] for _ in range(26)]
        result = 0
        for i, c in enumerate(s):
            curr = lookup[ord(c)-ord('a')]
            for j in range(i, len(s)):
                if s[j] != s[i]:
                    break
                if j-i+1 == len(curr):
                    curr.append(0)
                curr[j-i+1] += 1
                if curr[j-i+1] == 3:
                    result = max(result, j-i+1)
        return result if result else -1
