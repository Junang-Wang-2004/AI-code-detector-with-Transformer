# Time:  O(nlogn)
# Space: O(n)
class Solution2(object):
    def minAvailableDuration(self, slots1, slots2, duration):
        """
        """
        slots1.sort(key = lambda x: x[0])
        slots2.sort(key = lambda x: x[0])
        i, j = 0, 0
        while i < len(slots1) and j < len(slots2):
            left = max(slots1[i][0], slots2[j][0])
            right = min(slots1[i][1], slots2[j][1])
            if left+duration <= right:
                return [left, left+duration]
            if slots1[i][1] < slots2[j][1]:
                i += 1
            else:
                j += 1
        return []
