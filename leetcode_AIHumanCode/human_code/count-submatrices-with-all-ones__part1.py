# Time:  O(m * n)
# Space: O(n)

# mono stack
class Solution(object):
    def numSubmat(self, mat):
        """
        """
        def count(heights):
            result = curr = 0
            stk = []
            for i in range(len(heights)):
                while stk and heights[stk[-1]] >= heights[i]:
                    j = stk.pop()
                    curr -= (heights[j]-heights[i])*(j-(stk[-1] if stk else -1))
                stk.append(i)
                curr += heights[i]
                result += curr
            return result

        result = 0
        heights = [0]*len(mat[0])
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                heights[j] = heights[j]+1 if mat[i][j] == 1 else 0
            result += count(heights)
        return result


