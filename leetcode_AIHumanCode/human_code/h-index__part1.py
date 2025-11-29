# Time:  O(n)
# Space: O(n)

class Solution(object):
    def hIndex(self, citations):
        """
        """
        n = len(citations)
        count = [0] * (n + 1)
        for x in citations:
            # Put all x >= n in the same bucket.
            if x >= n:
                count[n] += 1
            else:
                count[x] += 1

        h = 0
        for i in reversed(range(0, n + 1)):
            h += count[i]
            if h >= i:
                return i
        return h

