# Time:  O(nlogn)
# Space: O(n)
import collections


# faster in sort by using more space
class Solution(object):
    def numberOfWeakCharacters(self, properties):
        """
        """
        lookup = collections.defaultdict(list)
        for a, d in properties:
            lookup[a].append(d)
        result = max_d = 0
        for a in sorted(iter(lookup.keys()), reverse=True):
            result += sum(d < max_d for d in lookup[a])
            max_d = max(max_d, max(lookup[a]))
        return result
