# Time:  O(nlogn)
# Space: O(n)
class Solution2(object):
    def maxChunksToSorted(self, arr):
        """
        """
        def compare(i1, i2):
            return arr[i1]-arr[i2] if arr[i1] != arr[i2] else i1-i2

        idxs = [i for i in range(len(arr))]
        result, max_i = 0, 0
        for i, v in enumerate(sorted(idxs, cmp=compare)):
            max_i = max(max_i, v)
            if max_i == i:
                result += 1
        return result

