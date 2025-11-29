# Time:  O(nlogn)
# Space: O(n)
# sort, mono stack
class Solution2(object):
    def visibleMountains(self, peaks):
        """
        """
        def is_covered(a, b):
            x1, y1 = a
            x2, y2 = b
            return x2-y2 <= x1-y1 and x1+y1 <= x2+y2

        peaks.sort()
        stk = []
        for i in range(len(peaks)):
            while stk and is_covered(peaks[stk[-1]], peaks[i]):
                stk.pop()
            if (i-1 == -1 or peaks[i-1] != peaks[i]) and (not stk or not is_covered(peaks[i], peaks[stk[-1]])):  # not duplicted and not covered
                stk.append(i)
        return len(stk)
            
