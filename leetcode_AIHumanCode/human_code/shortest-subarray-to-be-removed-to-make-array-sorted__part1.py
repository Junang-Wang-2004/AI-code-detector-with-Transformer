# Time:  O(n)
# Space: O(1)

class Solution(object):
    def findLengthOfShortestSubarray(self, arr):
        """
        """
        j = -1
        for j in reversed(range(1, len(arr))):
            if arr[j-1] > arr[j]:
                break
        else:
            return 0
        result = j
        for i in range(j):
            if i and arr[i] < arr[i-1]:
                break
            while j < len(arr) and arr[i] > arr[j]:
                j += 1
            result = min(result, (j-i+1)-2)
        return result


