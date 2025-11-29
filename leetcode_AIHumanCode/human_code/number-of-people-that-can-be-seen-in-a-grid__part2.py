# Time:  O(m * n)
# Space: O(m + n)
# mono stack
class Solution2(object):
    def seePeople(self, heights):
        """
        """
        def count(heights, i, stk):
            cnt = 0
            while stk and heights(stk[-1]) < heights(i):
                stk.pop()
                cnt += 1
            if stk:
                cnt += 1
            if stk and heights(stk[-1]) == heights(i):
                stk.pop()
            stk.append(i)
            return cnt
            
        result = [[0]*len(heights[0]) for _ in range(len(heights))]
        for i in range(len(heights)):
            stk = []
            for j in reversed(range(len(heights[0]))):
                result[i][j] += count(lambda x: heights[i][x], j, stk)     
        for j in range(len(heights[0])):
            stk = []
            for i in reversed(range(len(heights))):
                result[i][j] += count(lambda x: heights[x][j], i, stk)             
        return result


