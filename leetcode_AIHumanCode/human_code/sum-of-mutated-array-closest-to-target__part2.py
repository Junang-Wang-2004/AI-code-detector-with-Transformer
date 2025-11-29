# Time:  O(nlogn)
# Space: O(1)
class Solution2(object):
    def findBestValue(self, arr, target):
        """
        """
        arr.sort(reverse=True)
        max_arr = arr[0]
        while arr and arr[-1]*len(arr) <= target:
            target -= arr.pop()
        if not arr:
            return max_arr
        x = (target-1)//len(arr)
        return x if target-x*len(arr) <= (x+1)*len(arr)-target else x+1


