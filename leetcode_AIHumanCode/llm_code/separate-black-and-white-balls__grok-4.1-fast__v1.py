class Solution:
    def minimumSteps(self, s: str) -> int:
        count = 0
        ones_count = 0
        for char in s:
            if char == '0':
                count += ones_count
            else:
                ones_count += 1
        return count
