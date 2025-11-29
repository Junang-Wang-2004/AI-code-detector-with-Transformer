# Time:  O(n * 4^n)
# Space: O(1)

# iterative solution
class Solution(object):
    def letterCombinations(self, digits):
        """
        """
        if not digits:
            return []

        lookup = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        total = 1
        for digit in digits:
            total *= len(lookup[int(digit)])
        result = []
        for i in range(total):
            base, curr = total, []
            for digit in digits:
                choices = lookup[int(digit)]
                base //= len(choices)
                curr.append(choices[(i//base)%len(choices)])
            result.append("".join(curr))
        return result


