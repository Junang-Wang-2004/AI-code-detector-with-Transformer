# Time:  O(nlogn)
# Space: O(n)

class Solution(object):
    # @param {Interval[]} intervals
    # @return {integer}
    def minMeetingRooms(self, intervals):
        result, curr = 0, 0
        line = [x for i, j in intervals for x in [[i, 1], [j, -1]]]
        line.sort()
        for _, num in line:
            curr += num
            result = max(result, curr)
        return result


