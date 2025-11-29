# Time:  O(nlogn)
# Space: O(n)
# segment tree solution
class Solution2_TLE(object):
    def longestObstacleCourseAtEachPosition(self, obstacles):
        """
        """
        sorted_obstacles = sorted(set(obstacles))
        lookup = {x:i for i, x in enumerate(sorted_obstacles)}
        segment_tree = SegmentTree(len(lookup))
        result = []
        for x in obstacles:
            cnt = segment_tree.query(0, lookup[x])+1
            result.append(cnt)
            segment_tree.update(lookup[x], lookup[x], cnt)
        return result
