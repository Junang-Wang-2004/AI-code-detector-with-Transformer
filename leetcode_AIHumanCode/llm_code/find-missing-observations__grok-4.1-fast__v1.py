class Solution:
    def missingRolls(self, rolls, mean, n):
        existing_sum = sum(rolls)
        total_rolls = len(rolls) + n
        required_sum = mean * total_rolls
        needed_sum = required_sum - existing_sum
        if needed_sum < n or needed_sum > 6 * n:
            return []
        base = needed_sum // n
        extras = needed_sum % n
        result = []
        for i in range(n):
            if i < extras:
                result.append(base + 1)
            else:
                result.append(base)
        return result
