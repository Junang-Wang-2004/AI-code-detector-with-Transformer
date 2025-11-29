# Time:  O(m * n)
# Space: O(l), l is min(len(arr) for arr in arrays)

class Solution(object):
    def longestCommomSubsequence(self, arrays):
        """
        """
        result = min(arrays, key=lambda x: len(x))
        for arr in arrays:
            new_result = []
            i, j = 0, 0
            while i != len(result) and j != len(arr):
                if result[i] < arr[j]:
                    i += 1
                elif result[i] > arr[j]:
                    j += 1
                else:
                    new_result.append(result[i])
                    i += 1
                    j += 1
            result = new_result
        return result


