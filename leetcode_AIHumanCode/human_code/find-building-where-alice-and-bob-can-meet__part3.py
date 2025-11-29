# Time:  O(n + qlogn)
# Space: O(n + q)
# offline solution, mono stack, binary search
class Solution3(object):
    def leftmostBuildingQueries(self, heights, queries):
        """
        """
        def binary_search_right(left, right, check):
            while left <= right:
                mid = left + (right-left)//2
                if not check(mid):
                    right = mid-1
                else:
                    left = mid+1
            return right

        result = [-1]*len(queries)
        qs = [[] for _ in range(len(heights))]
        for i, (a, b) in enumerate(queries):
            if a > b:
                a, b = b, a
            if a == b or heights[a] < heights[b]:
                result[i] = b
            else:
                qs[b].append((heights[a], i))
        stk = []
        for b in reversed(range(len(heights))):
            while stk and stk[-1][0] <= heights[b]:
                stk.pop()
            stk.append((heights[b], b))
            for ha, i in qs[b]:
                j = binary_search_right(0, len(stk)-1, lambda x: stk[x][0] > ha)
                if j >= 0:
                    result[i] = stk[j][1]
        return result
