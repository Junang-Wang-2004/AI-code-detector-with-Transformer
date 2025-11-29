# Time:  O(m * n)
# Space: O(m + n)

# mono stack, optimized from solution2
class Solution(object):
    def seePeople(self, heights):
        """
        """
        def count(h, stk):
            cnt = 0
            while stk and stk[-1] < h:
                stk.pop()
                cnt += 1
            if stk:
                cnt += 1
            if not stk or stk[-1] != h:
                stk.append(h)
            return cnt
            
        result = [[0]*len(heights[0]) for _ in range(len(heights))]
        for i in range(len(heights)):
            stk = []
            for j in reversed(range(len(heights[0]))):
                result[i][j] += count(heights[i][j], stk)     
        for j in range(len(heights[0])):
            stk = []
            for i in reversed(range(len(heights))):
                result[i][j] += count(heights[i][j], stk)             
        return result


