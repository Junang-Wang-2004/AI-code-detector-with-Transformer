# Time:  O(n^2)
# Space: O(n)
class Solution2(object):
    def reconstructQueue(self, people):
        """
        """
        people.sort(key=lambda h_k1: (-h_k1[0], h_k1[1]))
        result = []
        for p in people:
            result.insert(p[1], p)
        return result

