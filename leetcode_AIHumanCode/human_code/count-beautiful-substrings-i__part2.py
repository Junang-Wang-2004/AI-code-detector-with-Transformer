# Time:  O(n^2)
# Space: O(1)
# brute force
class Solution2(object):
    def beautifulSubstrings(self, s, k):
        """
        """
        VOWELS = set("aeiou")
        result = 0
        for i in range(len(s)):
            c = v = 0
            for j in range(i, len(s)):
                if s[j] in VOWELS:
                    v += 1
                else:
                    c += 1
                if c == v and (c*v)%k == 0:
                    result += 1
        return result
    
