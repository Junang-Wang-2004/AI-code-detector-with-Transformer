# Time:  O(nlogn)
# Space: O(n)
# Segment Tree solution.
class Solution2(object):
    def fallingSquares(self, positions):
        index = set()
        for left, size in positions:
            index.add(left)
            index.add(left+size-1)
        index = sorted(list(index))
        tree = SegmentTree(len(index), max, max, 0)
        # tree = SegmentTree2([0]*len(index), max, max, 0)
        max_height = 0
        result = []
        for left, size in positions:
            L, R = bisect.bisect_left(index, left), bisect.bisect_left(index, left+size-1)
            h = tree.query(L, R) + size
            tree.update(L, R, h)
            max_height = max(max_height, h)
            result.append(max_height)
        return result


