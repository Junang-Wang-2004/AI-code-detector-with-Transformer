# Time:  O(nlogn)
# Space: O(n)
# mono stack + bottom-up dp + segment tree
class Solution3(object):
    def maxJumps(self, arr, d):
        """
        """
        left, decreasing_stk = list(range(len(arr))), []
        for i in range(len(arr)):
            while decreasing_stk and arr[decreasing_stk[-1]] < arr[i]:
                if i - decreasing_stk[-1] <= d:
                    left[i] = decreasing_stk[-1]
                decreasing_stk.pop()
            decreasing_stk.append(i)
        right, decreasing_stk = list(range(len(arr))), []
        for i in reversed(range(len(arr))):
            while decreasing_stk and arr[decreasing_stk[-1]] < arr[i]:
                if decreasing_stk[-1] - i <= d:
                    right[i] = decreasing_stk[-1]
                decreasing_stk.pop()
            decreasing_stk.append(i)

        segment_tree = SegmentTree(len(arr))
        for _, i in sorted([x, i] for i, x in enumerate(arr)):
            segment_tree.update(i, i, segment_tree.query(left[i], right[i]) + 1)
        return segment_tree.query(0, len(arr)-1)
