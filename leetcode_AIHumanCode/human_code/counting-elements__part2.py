# Time:  O(nlogn)
# Space: O(1)
class Solution(object):
    def countElements(self, arr):
        """
        """
        arr.sort()
        result, l = 0, 1
        for i in range(len(arr)-1):
            if arr[i] == arr[i+1]:
                l += 1
                continue
            if arr[i]+1 == arr[i+1]:
                result += l
            l = 1
        return result
