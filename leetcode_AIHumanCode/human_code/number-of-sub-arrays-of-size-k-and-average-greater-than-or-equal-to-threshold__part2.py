# Time:  O(n)
# Space: O(n)
class Solution2(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        """
        accu = [0]
        for x in arr:
            accu.append(accu[-1]+x)
        result = 0
        for i in range(len(accu)-k):
            if accu[i+k]-accu[i] >= threshold*k:
                result += 1
        return result
