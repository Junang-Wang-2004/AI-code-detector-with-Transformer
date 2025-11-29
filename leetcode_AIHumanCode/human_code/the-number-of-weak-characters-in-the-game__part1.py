# Time:  O(nlogn)
# Space: O(1)

class Solution(object):
    def numberOfWeakCharacters(self, properties):
        """
        """
        properties.sort(cmp=lambda a, b: cmp(b[1], a[1]) if a[0] == b[0] else cmp(a[0], b[0]))
        result = max_d = 0
        for a, d in reversed(properties):
            if d < max_d:
                result += 1
            max_d = max(max_d, d)
        return result

    
