# Time:  O(nlogn)
# Space: O(1)

class Solution(object):
    def findBestValue(self, arr, target):
        """
        """
        arr.sort(reverse=True)
        max_arr = arr[0]
        while arr and arr[-1]*len(arr) <= target:
            target -= arr.pop()
        # let x = ceil(t/n)-1
        # (1) (t/n-1/2) <= x:
        #    return x, which is equal to ceil(t/n)-1 = ceil(t/n-1/2) = (2t+n-1)//2n
        # (2) (t/n-1/2) > x:
        #    return x+1, which is equal to ceil(t/n) = ceil(t/n-1/2) = (2t+n-1)//2n
        # (1) + (2) => both return (2t+n-1)//2n
        return max_arr if not arr else (2*target+len(arr)-1)//(2*len(arr))


