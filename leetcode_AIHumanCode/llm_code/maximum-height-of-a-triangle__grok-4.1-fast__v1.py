class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        def feasible(height: int) -> bool:
            odd_levels = (height + 1) // 2
            even_levels = height // 2
            odd_blocks = odd_levels * odd_levels
            even_blocks = even_levels * (even_levels + 1)
            return (red >= odd_blocks and blue >= even_blocks) or \
                   (red >= even_blocks and blue >= odd_blocks)

        left, right = 0, 2000000000
        while left < right:
            mid = (left + right + 1) // 2
            if feasible(mid):
                left = mid
            else:
                right = mid - 1
        return left
