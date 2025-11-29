# Time:  O(nlogm), m is the max value of arr
# Space: O(logm)
class Solution2(object):
    def closestToTarget(self, arr, target):
        """
        """
        result, dp = float("inf"), set()  # at most O(logm) dp states
        for x in arr:
            dp = {x}|{f&x for f in dp}
            for f in dp:
                result = min(result, abs(f-target))
        return result
