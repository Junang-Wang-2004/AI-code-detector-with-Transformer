# Time:  O(m * n)
# Space: O(m + n)
# mono stack
class Solution3(object):
    def seePeople(self, heights):
        """
        """
        def count(heights, i, stk, add):
            while stk and heights(stk[-1]) < heights(i):
                increase(stk.pop())
            if stk:
                increase(stk[-1])
            if stk and heights(stk[-1]) == heights(i):
                stk.pop()
            stk.append(i)
            
        result = [[0]*len(heights[0]) for _ in range(len(heights))]
        for i in range(len(heights)):
            stk = []
            def increase(x): result[i][x] += 1
            for j in range(len(heights[0])):
                count(lambda x: heights[i][x], j, stk, add)
        for j in range(len(heights[0])):
            stk = []
            def increase(x): result[x][j] += 1
            for i in range(len(heights)):
                count(lambda x: heights[x][j], i, stk, add)
        return result
