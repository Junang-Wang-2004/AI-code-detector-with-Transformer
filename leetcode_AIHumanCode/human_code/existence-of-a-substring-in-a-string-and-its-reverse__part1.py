# Time:  O(n)
# Space: O(min(n, 26^2))

# hash table
class Solution(object):
    def isSubstringPresent(self, s):
        """
        """
        lookup = [[False]*26 for _ in range(26)]
        for i in range(len(s)-1):
            lookup[ord(s[i])-ord('a')][ord(s[i+1])-ord('a')] = True
        return any(lookup[ord(s[i+1])-ord('a')][ord(s[i])-ord('a')]  for i in range(len(s)-1))
    

