# Time:  O(n^2)
# Space: O(n)
class Solution4(object):
    def fallingSquares(self, positions):
        """
        """
        heights = [0] * len(positions)
        for i in range(len(positions)):
            left_i, size_i = positions[i]
            right_i = left_i + size_i
            heights[i] += size_i
            for j in range(i+1, len(positions)):
                left_j, size_j = positions[j]
                right_j = left_j + size_j
                if left_j < right_i and left_i < right_j:  # intersect
                    heights[j] = max(heights[j], heights[i])

        result = []
        for height in heights:
            result.append(max(result[-1], height) if result else height)
        return result

