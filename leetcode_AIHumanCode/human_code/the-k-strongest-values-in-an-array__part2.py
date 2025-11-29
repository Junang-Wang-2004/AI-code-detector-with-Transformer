# Time:  O(nlogn)
# Space: O(1)
class Solution2(object):
    def getStrongest(self, arr, k):
        """
        """
        arr.sort()
        m = arr[(len(arr)-1)//2]
        arr.sort(key=lambda x: (-abs(x-m), -x))
        return arr[:k]


