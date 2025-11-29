# Time:  O(m * n), m = 26
# Space: O(m * n)
class Solution2(object):
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        """
        """
        lookup = {}
        for right in range(minSize-1, len(s)):
            word = s[right-minSize+1:right+1]
            if word in lookup:
                lookup[word] += 1
            elif len(collections.Counter(word)) <= maxLetters:
                lookup[word] = 1
        return max(list(lookup.values()) or [0])
