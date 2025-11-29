# Time:  O(nlogn)
# Space: O(1)

class Solution(object):
    def getStrongest(self, arr, k):
        """
        """
        arr.sort()
        m = arr[(len(arr)-1)//2]
        result = []
        left, right = 0, len(arr)-1
        while len(result) < k:
            if m-arr[left] > arr[right]-m:
                result.append(arr[left])
                left += 1
            else:
                result.append(arr[right])
                right -= 1
        return result


