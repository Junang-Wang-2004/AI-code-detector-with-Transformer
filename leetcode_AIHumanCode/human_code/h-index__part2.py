# Time:  O(nlogn)
# Space: O(1)
class Solution2(object):
    def hIndex(self, citations):
        """
        """
        citations.sort(reverse=True)
        h = 0
        for x in citations:
            if x >= h + 1:
                h += 1
            else:
                break
        return h

