# Time:  O(n + 26^2)
# Space: O(26)
# freq table
class Solution3(object):
    def minimumDeletions(self, word, k):
        """
        """
        cnt = [0]*26
        for x in word:
            cnt[ord(x)-ord('a')] += 1
        return min(sum(y if y < x else max(y-(x+k), 0) for y in cnt if y) for x in cnt if x)
