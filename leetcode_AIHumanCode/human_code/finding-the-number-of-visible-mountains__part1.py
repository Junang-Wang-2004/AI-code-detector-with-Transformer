# Time:  O(nlogn)
# Space: O(1)

# math, sort
class Solution(object):
    def visibleMountains(self, peaks):
        """
        """
        peaks.sort(key=lambda x: (x[0]-x[1], -(x[0]+x[1])))  # rotate points by 45 degrees and we only care the largest new y in the same new x
        result = mx = 0
        for i in range(len(peaks)):
            if peaks[i][0]+peaks[i][1] <= mx:
                continue
            mx = peaks[i][0]+peaks[i][1]
            if i+1 == len(peaks) or peaks[i+1] != peaks[i]:
                result += 1
        return result


